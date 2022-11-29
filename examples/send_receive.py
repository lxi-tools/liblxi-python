#!/usr/bin/env python3

# liblxi-python test script

import lxi
import sys

max_msg_length = 5000
timeout = 3000

if len(sys.argv) != 2:
    print("Usage: %s <ip>" % sys.argv[0])
    exit()

# Initialize library
lxi.init()

# Connect to device
device = lxi.connect(sys.argv[1], 0, "inst0", timeout, lxi.protocol.VXI11)

# Send command
command = "*IDN?"
status = lxi.send(device, command, len(command), timeout)
print("Sent " + str(status) + " bytes")
print("Sent command: " + str(command))

# Receive command response
status, message = lxi.receive(device, max_msg_length, timeout)
print("Received " + str(status) + " bytes")
print("Received message: " + message)

# Disconnect
lxi.disconnect(device)

