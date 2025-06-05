#! /bin/bash

if [[ -z "$(ps -e | grep "anki")" ]]; then
    /var/lib/flatpak/exports/bin/net.ankiweb.Anki 1> /dev/null 2> /dev/null &
fi

SCRIPT_LOCATION="$(dirname "$(realpath "$0")")"
echo $SCRIPT_LOCATION
gnome-screenshot --area --file="$SCRIPT_LOCATION/img.png"
tesseract "$SCRIPT_LOCATION/img.png" "$SCRIPT_LOCATION/out"

DECKS="$(curl -X POST  --silent http://127.0.0.1:8765 \
   -H 'Content-Type: application/json' \
   -d '{"action": "deckNames","version": 6}' | jq -c .result | sed -e 's/\[\|\]/ /g' -e 's/,/!/g' -e 's/"!"/!/g' -e 's/"//g')"

SCRIPT_LOCATION="$(dirname "$(realpath "$0")")"

yad \
--title="Add to anki" \
--form \
--image="$SCRIPT_LOCATION/img.png" \
--field="Back:CHK" true \
--field="Deck:CBE" "${DECKS}" \
--field="Front" \
--field="Back" \
--button="Save:0" \
--button="Cancel:1" > "$SCRIPT_LOCATION/card.txt" && "$SCRIPT_LOCATION/pdf_to_anki.py" < "$SCRIPT_LOCATION/card.txt" 1> "$SCRIPT_LOCATION/debug.txt" 2> "$SCRIPT_LOCATION/debug.txt"