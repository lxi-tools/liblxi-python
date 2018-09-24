import liblxi
timeout=5
command = "*IDN?"
response = 65536*" "

liblxi.init()
device = liblxi.connect( "10.42.0.42", 0, "inst0", timeout, liblxi.ProtocolType.VXI11);
liblxi.send( device, command, len(command), timeout )
liblxi.receive(device, response, len(response), timeout)
print response
liblxi.disconnect()
