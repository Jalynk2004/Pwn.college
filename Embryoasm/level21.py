from pwn import *

context.log_level='info'
context.arch='amd64'
p = process("/challenge/embryoasm")
assembly = """
    cmp rdi, 0
    je endloop
whileloop:
    mov rbx,[rdi]
    cmp rbx, 0
    je endloop
    inc rax
    inc rdi
    jmp whileloop
endloop:
    nop
"""
code = asm(assembly)
p.send(code)
p.interactive()
