#!/usr/bin/env python

import os
import json
import requests
from time import sleep

CWD = os.path.dirname(os.path.abspath(__file__)) + '/'

song_queue = 'https://api.streamersonglist.com/v1/streamers/arighi_violin/queue'

template = """
<html>
<head>
  <meta http-equiv="refresh" content="5">
</head>
<body>
<p style="color:white;font-size:22px">%s</p>
</body>
</html>
"""

def main():
    while True:
        r = requests.get(song_queue)
        data = json.loads(r.text)
        try:
            user = data["list"][0]["requests"][0]["name"]
            song = data["list"][0]["song"]
            if song is None:
                song = data["list"][0]["nonlistSong"]
                text = 'Live-learn: "<i>%s</i>" requested by <b>%s</b>' % \
                       (song, user)
            else:
                title = song["title"]
                artist = song["artist"]
                text = 'Now playing: "<i>%s - %s</i>" requested by <b>%s</b>' % \
                       (song["title"], song["artist"], user)
        except:
            text = "No song is being played (just chatting/practicing...)"
        with open(CWD + '.index.html', 'w') as fd:
            fd.write(template % text)
        os.rename(CWD + '.index.html', CWD + 'index.html')
        print(text)
        sleep(10)

if __name__ == '__main__':
    main()

