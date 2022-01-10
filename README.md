# python-liblxi

Python bindings for liblxi.

## Features

The python bindings implements all of the liblxi API except the discover
functions.

## Requirements

Make sure you have python3 and liblxi installed.

## Installation

### Linux

Install in Linux Debian based (Ubuntu, etc.):
```
sudo apt install liblxi1 python3
```

For other Linux distributions, consult your package manager tool.

### FreeBSD

Install in FreeBSD:
```
pkg install liblxi python3
```

## Run the example code

First, edit test.py to replace the hardcoded IP address with the IP of your instrument, then run:
```
$ python3 test.py
Siglent Technologies,SDG2042X,SDG2XCAC2R0212,2.01.01.23R7
```

If it fails to find the liblxi library you can try preload it like so:

```
LD_PRELOAD=/usr/lib/liblxi.so python3 test.py
```
