#! /bin/bash

DECKS="$(curl -X POST  --silent http://127.0.0.1:8765 \
   -H 'Content-Type: application/json' \
   -d '{"action": "deckNames","version": 6}' | jq -c .result | sed -e 's/\[\|\]/ /g' -e 's/,/!/g' -e 's/"!"/!/g' -e 's/"//g')"

echo ${DECKS}
SCRIPT_LOCATION="$(dirname "$(realpath "$0")")"

yad \
--title="Add to anki" \
--form \
--image="$SCRIPT_LOCATION/img.png" \
--field="Back:CHK" true \
--field="Deck:CBE" "${DECKS}" \
--field="Front" \
--field="Back" \
--button="Add Image:2" \
--button="Save:0" \
--button="Cancel:1" 