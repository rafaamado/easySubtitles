#!/usr/bin/env python
# coding: utf-8

# Rafael Henrique Amado
# Github: https://github.com/rafaamado
# Easy API docs: 
# http://pt.thesubdb.com/api/

import sys
import os
import hashlib
import requests

#folder = r'C:\Users\Rafael\Videos'

#this hash function receives the name of the file and returns the hash code
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

def downloadSubtitle(filePath, languages):
    headers = {
        'User-Agent': 'SubDB/1.0 (Pyrrot/0.1; http://github.com/jrhames/pyrrot-cli)',
        'From': 'youremail@domain.com'
    }
    params = [('hash',  get_hash(filePath)) , ('language', languages)   ]

    r = requests.get("http://api.thesubdb.com/?action=download", params=params, headers=headers)
    print(r)
    if r.status_code == 200:
        strPath = os.path.splitext(filePath)[0]+'.srt'

        f = open(strPath, 'wb')
        f.write(r.content)
        f.close()


if (len(sys.argv) < 3) :
    print('Folder and language parameter expected! Ex: python easySub.py C:\MyVideos en')
    print('Languages: en,es,fr,it,nl,pl,pt,ro,sv,tr')
    sys.exit()

folder = sys.argv[1]
languages = sys.argv[2] # 'en'
print (folder)

for file in os.listdir(folder):
    if file.endswith((".mp4", ".avi", ".mkv", ".wmv", ".rmvb")):
        print(os.path.join(folder, file))
        downloadSubtitle(os.path.join(folder, file), languages)



