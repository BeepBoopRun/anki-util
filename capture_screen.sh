#! /bin/bash

if [[ -z "$(ps -e | grep "anki")" ]]; then
    /var/lib/flatpak/exports/bin/net.ankiweb.Anki 1> /dev/null 2> /dev/null &
fi

SCRIPT_LOCATION="$(dirname "$(realpath "$0")")"
gnome-screenshot --area --file="$SCRIPT_LOCATION/img.png"
tesseract "$SCRIPT_LOCATION/img.png" "$SCRIPT_LOCATION/out"
sh "$SCRIPT_LOCATION/popup.sh"