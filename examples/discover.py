#!/usr/bin/env python3

# liblxi-python discover example script

import lxi


# Callback functions which are called during discovery

def broadcast(address, interface):
    address = str(address, 'ascii')
    interface = str(interface, 'ascii')
    print("Broadcasting on " + interface + " using address " + address)
    return

def device(address, id):
    address = str(address, 'ascii')
    id = str(id, 'ascii')
    print("   Found " + id + " on address " + address)
    return

def service(address, id, service, port):
    address = str(address, 'ascii')
    id = str(id, 'ascii')
    service = str(service, 'ascii')
    port = str(port)
    print("Found " + id + " on address " + address)
    print(" " + service + " service on port " + port)

# Initialize library
lxi.init()

# Search for devices
timeout = 1000
info = lxi.lxi_info_class()
info.broadcast = broadcast
info.device = device
info.service = service

device = lxi.discover(info, timeout, lxi.discover_protocol.DISCOVER_VXI11)
# device = lxi.discover(info, timeout, lxi.discover_protocol.DISCOVER_MDNS)

