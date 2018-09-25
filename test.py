import liblxi
my_ip = "1.2.3.4" # IP of your instrument
timeout=5
command = "*IDN?"
response = 200*" "

liblxi.init()
device = liblxi.connect( my_ip, 0, "inst0", timeout, liblxi.ProtocolType.VXI11);
liblxi.send( device, command, len(command), timeout )
liblxi.receive(device, response, len(response), timeout)
print response
liblxi.disconnect( device )
# with a siglent siggen this outputs
# Siglent Technologies,SDG2042X,SDG2XCAC2R0212,2.01.01.23R7

