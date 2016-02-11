# Basic Web Services Example
# Note does not work. Not supported any longer.

import gdata.youtube
import gdata.youtube.service

# YouTubeService generates and object to communicate with the youtube api
youtube_service=gdata.youtube.service.YouTubeService()

# prompt the user for a Youtube user ID
playlist= raw_input("Please enter the user ID: ")

# setup the actual api call
url="http://gdata.youtube.com/feeds/api/users/"
playlist_url=url+playlist+"/playlists"

# retrieve the playlist
video_feed=youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print "\nPlaylists for {}:\n".format(playlist)

for p in video_feed.entry:
    print p.title.text
