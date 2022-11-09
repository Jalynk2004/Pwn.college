from pwn import *
context.log_level='info'
context.arch='amd64'

p = process ("/challenge/embryoasm")
assembly = """
    jmp relative
    .rept 0x51
    nop
    .endr
relative:
    mov rdi, [rsp]
    mov rcx, 0x403000
    jmp rcx
"""
code = asm(assembly)
p.send(code)
p.interactive()

