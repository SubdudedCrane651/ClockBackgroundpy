#!/bin/bash
#brew install create-dmg
APP_NAME = "Desktop_Countdown"
sudo rm -rf Desktop_Countdown.dmg dist build
sudo rm -rf build dist
sudo python3 setup.py py2app
sudo xattr -dr com.apple.quarantine "dist/${APP_NAME}.app"
sudo create-dmg \
  --volname "Desktop Countdown Installer" \
  --window-pos 200 120 \
  --window-size 600 400 \
  --icon-size 100 \
  --app-drop-link 400 200 \
  Desktop_Countdown.dmg \
  dist/Desktop_Countdown.app

