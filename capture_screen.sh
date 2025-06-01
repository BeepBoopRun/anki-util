#! /bin/bash

SCRIPT_LOCATION="$(dirname "$(realpath "$0")")"
gnome-screenshot --area --file="$SCRIPT_LOCATION/img.png"
tesseract "$SCRIPT_LOCATION/img.png" "$SCRIPT_LOCATION/out"