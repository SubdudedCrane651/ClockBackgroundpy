#!/bin/bash

set -e

APP_NAME="Desktop_Countdown"
VERSION="1.0"

echo "=== Cleaning old builds ==="
sudo rm -rf build dist Countdown_Pkg "$APP_NAME.pkg"

echo "=== Running py2app ==="
python3 setup.py py2app

echo "=== Creating installer folder structure ==="
sudo mkdir -p Countdown_Pkg/Applications

echo "=== Copying .app bundle ==="
sudo cp -R "dist/${APP_NAME}.app" "Countdown_Pkg/Applications/${APP_NAME}.app"

echo "=== Removing quarantine flags ==="
sudo xattr -dr com.apple.quarantine "Countdown_Pkg/Applications/${APP_NAME}.app"

echo "=== Building .pkg installer ==="
sudo pkgbuild \
  --root Countdown_Pkg \
  --identifier "com.richard.${APP_NAME}" \
  --version "$VERSION" \
  --install-location "/" \
  "${APP_NAME}.pkg"

echo "=== Build complete ==="
echo "Installer created: ${APP_NAME}.pkg"
