# Fedora-OSTree-Setup

A python-program that automates the setup of Fedora Silverblue/Kinoite
based on given config file.

## Why this is needed
An OSTree-based Fedora system can result in a pretty perfect and unbreakable experience.
- Your system stays pretty much the same as the developers version. This makes bugfixes and support easier.
- You install external Apps as Flatpaks or through Podman containers. You can use any Flatpak, Ubuntu, Fedora, Arch e.g. apps you want, but they can't break your system
- The system can update automatically, if an update breaks something, you can reboot and use the older version.

But Fedora Kinoite/Silverblue are not well setup out of the box. 
- Apps dont autoupdate
- Native Firefox installed but it can't play Videos
- adding COPR repositories or other external ones is complicated
- changing the SDDM theme is not possible
- All licensed drivers and codecs are missing, especially on NVIDIA
- Some preinstalled apps may have better alternatives
- The Android emulator Waydroid is very complicated to install
- The standard shell "bash" is behind "fish" in user experience
- Users need to enter a password for many tasks
- and many more...

**We aim to fix all of these issues with this project!**

To speed up updates the goal are ready modified Images you can use, and a script applying some settings you can decide.

# Contributing

All contributions whether small or large is welcome! Just fork the
project and create a pull request when done.

Refer to [HACKING.md](HACKING.md) to start in how to setup the project,
then in [CONTRIBUTING.md](CONTRIBUTING.md) for protocols/guidelines to
follow, and take a browse in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
to see what is the acceptable behavior in the community.
