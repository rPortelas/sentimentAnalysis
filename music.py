import soundcloud
import vlc

import re



# create a client object with your app credentials
client = soundcloud.Client(client_id='WGvWDXJhUeRcmnawwdMDyTcbUmH8IHpS')


# find all sounds of buskers licensed under 'creative commons share alike'
tracks = client.get('/tracks', q='sad instrumental', license='cc-by-sa')

# fetch track to stream
track = tracks[1]
print(tracks)

# get the tracks streaming URL
stream_url = client.get(track.stream_url, allow_redirects=False)

# print the tracks stream URL
print stream_url.location

song = stream_url.location

song = re.sub('s','',song,1)

print song


p = vlc.MediaPlayer(song)
p.play()


