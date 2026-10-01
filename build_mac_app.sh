#!/bin/bash

set -e

APP_NAME="Desktop_Countdown"
VERSION="1.0"

echo "=== Cleaning old builds ==="
rm -rf build dist Countdown_Pkg "$APP_NAME.pkg"

echo "=== Running py2app ==="
python3 setup.py py2app

echo "=== Creating installer folder structure ==="
mkdir -p Countdown_Pkg/Applications

echo "=== Copying .app bundle ==="
cp -R "dist/${APP_NAME}.app" "Countdown_Pkg/Applications/${APP_NAME}.app"

echo "=== Removing quarantine flags ==="
xattr -dr com.apple.quarantine "Countdown_Pkg/Applications/${APP_NAME}.app"

echo "=== Building .pkg installer ==="
pkgbuild \
  --root Countdown_Pkg \
  --identifier "com.richard.${APP_NAME}" \
  --version "$VERSION" \
  --install-location "/" \
  "${APP_NAME}.pkg"

echo "=== Build complete ==="
echo "Installer created: ${APP_NAME}.pkg"
