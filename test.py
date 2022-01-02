#####################################
#     python-liblxi test script     #
#####################################
#
# Make sure that liblxi is installed:
#
#  $ sudo apt install liblxi1
#
# Run script using Python v3.x:
#
#  $ python3 test.py
#

import lxi

max_msg_length = 5000
timeout = 3000

# Initialize library
lxi.init()

# Connect to device
device = lxi.connect("192.168.0.107", 0, "inst0", timeout, lxi.protocol.VXI11)

# Send command
command = "*IDN?"
status = lxi.send(device, command, len(command), timeout)
print("Sent command: " + str(command))
print("Sent " + str(status) + " bytes")

# Receive command response
status, message = lxi.receive(device, max_msg_length, timeout)
print("Received message: " + message)
print("Received " + str(status) + " bytes")

# Disconnect
lxi.disconnect(device)

