#!/bin/bash
#brew install create-dmg
rm -rf build dist
python3 setup.py py2app
create-dmg \
  --volname "Desktop Countdown Installer" \
  --window-pos 200 120 \
  --window-size 600 400 \
  --icon-size 100 \
  --app-drop-link 400 200 \
  Desktop_Countdown.dmg \
  dist/Desktop_Countdown.app
