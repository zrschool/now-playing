# now-playing
A web application that allows streamers to display what song is being played in realtime.

*****

# How It Works
now-playing prompts a user to input their last.fm username, a refresh interval, and a style preset, before generating a link that can be added as a browser source in various streaming software. now-playing will then make calls to the Last.fm API to determine information about the track a user is currently playing (or most recently played) and display them on the page. The page periodically refreshes based on the user's input refresh interval and takes the appearance of the user's chosen style preset. Addiional or alternate CSS can be added through certain streaming software.

*****

# Getting Started
The now-playing-element website is now offline, but users may host a local server from their desktop. now-playing makes use of the [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download), so users who wish to run now-playing locally must first install it from the link provided and start their local server with ``dev_appserver app.yaml`` in a shell with now-playing as the current working directory. The user will also need to create a python file called lastfm_api_key.py with a valid Last.fm API key which can be acquired [here](https://www.last.fm/api/account/create). Once the server is running, the user can visit the site (at localhost:8080 by default) and follow the instructions there to generate their stream element.
