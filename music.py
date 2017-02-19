import soundcloud
import vlc

# create a client object with your app credentials
client = soundcloud.Client(client_id='WGvWDXJhUeRcmnawwdMDyTcbUmH8IHpS')


# find all sounds of buskers licensed under 'creative commons share alike'
tracks = client.get('/tracks', q='buskers', license='cc-by-sa')

# fetch track to stream
track = tracks[0]

# get the tracks streaming URL
stream_url = client.get(track.stream_url, allow_redirects=False)

# print the tracks stream URL
print stream_url.location

p = vlc.MediaPlayer(stream_url.location)
p.play()