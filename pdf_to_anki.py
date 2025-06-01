#! /bin/python

import genanki
import requests
import sys
import time
import shutil

if(len(sys.argv) < 2):
    print("Specify the necesarry arguments!")

ANKI_USER_PATH = "/home/zcrank/.var/app/net.ankiweb.Anki/data/Anki2/User 1/"

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Front'},
    {'name': 'Back'},
    {'name': 'BookPages'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Back}}<br>{{BookPages}}',
    },
  ])

hash = int(time.time())
anki_img_path = f"{ANKI_USER_PATH}/collection.media/{hash}.png"
shutil.copyfile("img.png", anki_img_path)


my_fields = ["non", "omnis"]
my_fields.append(f'<img src="{hash}.png">')

my_note = genanki.Note(
  model=my_model,
  fields=my_fields)


my_deck = genanki.Deck(
  2059400110,
  'Advanced Toolkit for Bioinformatics')

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
