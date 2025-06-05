#! /bin/python

import genanki
import requests
import sys
import time
import shutil
import hashlib


for x in sys.argv:
    print(x)

    
if(len(sys.argv) < 2):
    print("No input given!")
    sys.exit(1)

input = sys.argv[1].split("|")
on_back = bool(input[0])
deck = input[1]
front = input[2]
back = input[3]

ANKI_USER_PATH = "/home/zcrank/.var/app/net.ankiweb.Anki/data/Anki2/User 1/"

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Front'},
    {'name': 'Back'},
    {'name': 'Image'},
    {'name': 'OCR'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Back}}<br>{{Image}}',
    },
  ])

img_hash = int(time.time())
anki_img_path = f"{ANKI_USER_PATH}/collection.media/{img_hash}.png"
shutil.copyfile("img.png", anki_img_path)

my_fields = [sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ""]
my_fields.append(f'<img src="{img_hash}.png">')

with open("out.txt", "r") as f:
    my_fields.append(f.read())


my_note = genanki.Note(
  model=my_model,
  fields=my_fields)

deck_name = deck
deck_hash = int(hashlib.md5(deck_name.encode('utf-8')).hexdigest(), 16) % (2^16) + 1

my_deck = genanki.Deck(
  deck_hash,
  deck_name)

my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file(f'{ANKI_USER_PATH}/data/Deck.apkg')

response = requests.post("http://127.0.0.1:8765", json={
    "action": "importPackage",
    "version": 6,
    "params": {
        "path": f'{ANKI_USER_PATH}/data/Deck.apkg'
    }
})

print(response)
print(response.json())
