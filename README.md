# python-liblxi

Initial attempt at python bindings for liblxi. 

## liblxi is a submodule of this git repo

after checkout of python-liblxi you need:

'''
$ git submodule init
$ git submodule update
'''

## cmake out-of-source build

Note: the config.h is built by autogen/configure - not currently produced by cmake.

'''
$ mkdir bld
$ cd bld
$ cmake ..
$ make
$ sudo make install
'''

## python test

'''
>>> import liblxi
>>> liblxi.init()
'''
