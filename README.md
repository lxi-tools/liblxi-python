# liblxi-python

Python bindings for liblxi.

## Requirements

Make sure you have python3 and liblxi installed.

## Installation

To use the liblxi python bindings script put it next to your script or add the
location of lxi.py to your PYTHONPATH variable. Also install the required
dependencies as described below.

### Linux

Install on Linux Debian based (Ubuntu, etc.):
```
sudo apt install liblxi1 python3
```

For other Linux distributions, consult your package manager tool.

### FreeBSD

Install on FreeBSD:
```
pkg install liblxi python3
```

## Run the example code

Note:

If it fails to find the liblxi library you can try preload it with the specific
path to the library. For example:

```
$ LD_PRELOAD=$HOME/opt/lib/liblxi.so PYTHONPATH=. python3 ./examples/send_receive.py 192.168.0.157
```

### Send and receive example

Run the example test script with the IP of your instrument as argument:
```
$ PYTHONPATH=. python3 ./examples/send_receive.py 192.168.0.157
Sent 5 bytes
Sent command: *IDN?
Received 49 bytes
Received message: Rohde&Schwarz,RTB2004,1333.1005k04/113192,02.400
```

### Discover example

Search for instruments:
```
$ PYTHONPATH=. python3 ./examples/discover.py
Broadcasting on lo using address 127.0.0.1
Broadcasting on enxe4b97a86fdad using address 192.168.0.255
   Found Rohde&Schwarz,NGM202,3638.4472k03/101403,03.068 00A8F863604 on address 192.168.0.107
Broadcasting on virbr0 using address 192.168.122.255
```
