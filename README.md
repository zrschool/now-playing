# now-playing
A web application that allows streamers to display what song is being played in realtime.

*****

# How It Works
now-playing prompts a user to input their last.fm username, a refresh interval, and a style preset, before generating a link that can be added as a browser source in various streaming software. now-playing will then make calls to the Last.fm API to determine information about the track a user is currently playing (or most recently played) and display them on the page. The page periodically refreshes based on the user's input refresh interval and takes the appearance of the user's chosen style preset. Addiional or alternate CSS can be added through certain streaming software.

*****

# Getting Started
Users may either use the now-playing website (coming soon.) or host a local server from their desktop. now-playing makes use of the [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download), so users who wish to run now-playing locally must first install it from the link provided and start their local server with ``dev_appserver app.yaml`` in a shell with now-playing as the current working directory directory.
