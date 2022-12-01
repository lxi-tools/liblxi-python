#
# Copyright (c) 2021  Keep It Simple Solutions
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holders nor contributors may be
#    used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

#
# Python bindings for liblxi
#

from ctypes import *
from ctypes.util import find_library

# Find library
liblxi = find_library('lxi')
if not liblxi:
    print("Could not find liblxi library")
    exit()

# Load the library
lib = cdll.LoadLibrary(liblxi)

# Define functions
def init():
    lib.lxi_init()

# Define types
class LXI_INFO(Structure):
    _fields_ = [("broadcast", CFUNCTYPE(None, c_char_p, c_char_p )),
                ("device", CFUNCTYPE(None, c_char_p, c_char_p)),
                ("service", CFUNCTYPE(None, c_char_p, c_char_p, c_char_p, c_int))]

class lxi_info_class:
    def broadcast(self, address, interface):
        return

    def device(self, address, id):
        return

    def service(self, address, id, service, port):
        return

def discover(info: lxi_info_class, timeout: int, type: int):
    lib.lxi_discover.argtypes = c_void_p, c_int, c_int
    lib.lxi_discover.restype = c_int
    BROADCAST_FUNC = CFUNCTYPE(None, c_char_p, c_char_p)
    broadcast_func = BROADCAST_FUNC(info.broadcast)
    DEVICE_FUNC = CFUNCTYPE(None, c_char_p, c_char_p)
    device_func = DEVICE_FUNC(info.device)
    SERVICE_FUNC = CFUNCTYPE(None, c_char_p, c_char_p, c_char_p, c_int)
    service_func = SERVICE_FUNC(info.service)
    c_info_p = pointer(LXI_INFO(broadcast_func, device_func, service_func))
    status = lib.lxi_discover(c_info_p, c_int(timeout), c_int(type))
    return status

def connect(address, port: int, name, timeout: int, protocol: int):
    lib.lxi_connect.argtypes = c_char_p, c_int, c_char_p, c_int, c_int
    lib.lxi_connect.restype = c_int
    address_bytes = str.encode(address, "ascii")
    name_bytes = str.encode(name, "ascii")
    device = lib.lxi_connect(address_bytes, c_int(port), name_bytes, c_int(timeout), c_int(protocol))
    return device

def send(device: int, message, length: int, timeout: int):
    lib.lxi_send.argtypes = c_int, c_char_p, c_int, c_int
    lib.lxi_send.restype = c_int
    message_bytes = str.encode(message)
    status = lib.lxi_send(c_int(device), message_bytes, c_int(length), c_int(timeout))
    return status

def receive(device: int, length: int, timeout: int):
    lib.lxi_receive.argtypes = c_int, c_char_p, c_int, c_int
    lib.lxi_receive.restype = c_int
    message_p = create_string_buffer(length)
    status = lib.lxi_receive(c_int(device), message_p, c_int(length), c_int(timeout))
    message = str(message_p.value,"ascii")
    return status, message

def disconnect(device: int):
    lib.lxi_disconnect.argtypes = (c_int,)
    lib.lxi_disconnect.restype = c_int
    status = lib.lxi_disconnect(device)
    return status

class _protocol_:
    def __init__(self):
        self.VXI11 = 0
        self.RAW = 1

protocol = _protocol_()

class _discover_protocol_:
    def __init__(self):
        self.DISCOVER_VXI11 = 0
        self.DISCOVER_MDNS = 1

discover_protocol = _discover_protocol_()
