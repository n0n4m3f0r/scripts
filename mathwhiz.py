import socket
import telnetlib
from struct import pack
 
 
 
s = socket.socket()
s.connect(('mathwhiz_c951d46fed68687ad93a84e702800b7a.quals.shallweplayaga.me',21249))
ll = ["ONE","TWO","THREE"]
lll = ["1","2","3"]
while True :
	x = s.recv(1024)
	if '[' in x : 
		x=x.replace('[','(').replace(']',')')
	
	if '{' in x :
		x=x.replace('{','(').replace('}',')')
	if '^' in x :
		x = x.replace('^','**')
	for i in range(0,len(ll)-1) : 
		if ll[i] in x :
			x = x.replace(ll[i],lll[i])
	
	if 'flag' in x : 
		print x 
		break
	
	xx = x.strip().split('=')
	
	res = eval(xx[0])
	
	s.send(str(res)+'\n') 
#You won!!!
#The flag is: Farva says you are a FickenChucker and you'd better watch Super Troopers 2
#awesome eval ;P
