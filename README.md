# python-liblxi

Simple python bindings for liblxi.

Note: Does not include discovery feature (yet).

## Requirements

Make sure you have python3 and liblxi installed:

```
sudo apt install liblxi1 python3
```

## Run the example code

```
$ python3 test.py
Siglent Technologies,SDG2042X,SDG2XCAC2R0212,2.01.01.23R7
```

If it fails to find the liblxi library you can try preload it like so:

```
LD_PRELOAD=/usr/lib/liblxi.so python3 test.py
```
