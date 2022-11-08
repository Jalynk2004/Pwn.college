from pwn import *
context.arch='amd64'
context.log_level='info'
p = process ("/challenge/embryoasm")
assembly = """
    add rax, [rsp]
    add rax, [rsp+0x8]
    add rax, [rsp+0x10]
    add rax, [rsp+0x18]

    mov rbx, 4
    div rbx

    push rax
"""
code = asm(assembly)
p.send(code)
p.interactive()
