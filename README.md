# Hash Generator

This program generate hashes from random salts.

<img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2F7%2F7%2F8%2F86920.jpg&f=1&nofb=1" alt="A very beautiful pikachu" />

## How to install

Install this program using python 3 and pip:

```pip install .```

In the future, this program will be available for linux and macOS using the most common package managers.

## How to use

The command to use this tools is `pg`. There is some options:

- `list`: get a list of algorithms allowed
- `generate`: generate a bcrypt algorithm by default

### How to use an specific algorithm

There is some flags for the `generate` option:

- `-a` or `--algorithm`: choose the algorithm to use
- `-d` or `--difficulty`: choose the difficulty of the algorithm from 1 to 10
