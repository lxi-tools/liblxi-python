import lxi

max_msg_length = 5000
timeout = 3000
command = "*IDN?"

lxi.init()

device = lxi.connect("192.168.0.107", 0, "inst0", timeout, 0)

status = lxi.send(device, command, len(command), timeout)
print("Sent command: " + str(command))
print("Sent " + str(status) + " bytes")

status, message = lxi.receive(device, max_msg_length, timeout)
print("Received message: " + message)
print("Received " + str(status) + " bytes")

lxi.disconnect(device)

