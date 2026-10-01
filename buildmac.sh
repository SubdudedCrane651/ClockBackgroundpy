#!/bin/bash
sudo rm -rf Countdown_Pkg Desktop_Countdown.pkg
sudo mkdir -p Countdown_Pkg
sudo ditto dist/Desktop_Countdown.app Countdown_Pkg/Desktop_Countdown.app
sudo xattr -w com.apple.bundle true Countdown_Pkg/Desktop_Countdown.app
sudo pkgbuild \
  --root Countdown_Pkg \
  --identifier com.richard.desktopcountdown \
  --version 1.0 \
  --install-location / \
  Desktop_Countdown_component.pkg

  sudo productbuild \
  --distribution distribution.xml \
  --package-path . \
  Desktop_Countdown.pkg
