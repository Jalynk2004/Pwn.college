from pwn import *

context.log_level='info'
context.arch='amd64'

p = process("/challenge/embryoasm")
assembly="""
    cmp rdi, 3
    jg trigger
    mov rax, rdi
    mov rcx, 8
    mul rcx
    add rax, rsi
    jmp [rax]
    jmp exit
trigger:
    jmp [rsi+32]
    jmp exit
exit:
    nop
"""
code = asm(assembly)
p.send(code)
p.interactive()
