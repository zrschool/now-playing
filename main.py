import math
import os
import logging
import xml.etree.ElementTree as ET
import webapp2
import jinja2

from urllib import urlopen

from lastfm_api_key import api_key


# Set up jinja environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class NowPlayingPage(webapp2.RequestHandler):
    def get(self):
        # Assign URL query parameters to variables
        lastfm_username = self.request.get("username")
        refresh_delay = self.request.get("delay")
        style_preset = self.request.get("preset")

        # Open last.fm recent tracks page and assign information to variables
        recent_tracks_url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+str(lastfm_username)+"&api_key="+str(api_key)+"&limit=1"
        tree = ET.parse(urlopen(recent_tracks_url))
        root = tree.getroot()
        try: # Attempt to fetch data from last.fm
            artist = root[0][0][0].text
            track = root[0][0][1].text
            artwork = root[0][0][8].text
        except: # Catch if data not returned
            logging.info("Out of Bounds Error")
            artist = "Artist Not Found"
            track = "Track Not Found"
            artwork = ""

        template_vars = {
            "artist" : artist,
            "track" : track,
            "artwork" : artwork,
            "preset" : style_preset,
        }

        template = jinja_env.get_template("templates/now_playing.html")
        self.response.write(template.render(template_vars))



class SetupPage(webapp2.RequestHandler):
    def get(self):
        # Assign URL query parameters to variables. Set 5000 as default delay
        username = self.request.get("username")
        delay = self.request.get("delay")
        if delay == "" or int(delay) == math.isnan:
            delay = 5000
        preset = self.request.get("preset")

        # Generate a link when button clicked. Element hidden before URL
        # query parameters are filled.
        now_playing_link = ""
        is_hidden = "is_hidden"
        if username != "":
            now_playing_link = "localhost:8080/now_playing?username=" + str(username) + "&delay=" + str(delay) + "&preset=" + str(preset)
            is_hidden = "visible"

        template_vars = {
            "now_playing_link" : now_playing_link,
            "is_hidden" : is_hidden,
        }

        template = jinja_env.get_template("templates/setup.html")
        self.response.write(template.render(template_vars))

    def post(self):
        # Fill query parameters and generate now playing link
        lastfm_username = self.request.get("lastfm-username")
        try:
            refresh_delay = self.request.get("refresh-delay")
        except:
            refresh_delay = 5000
        style_preset = self.request.get("style-preset")
        self.redirect("/?username=" + lastfm_username + "&delay=" + refresh_delay + "&preset=" + style_preset)


app = webapp2.WSGIApplication([
    ("/", SetupPage),
    ("/now_playing", NowPlayingPage),
], debug=True)
