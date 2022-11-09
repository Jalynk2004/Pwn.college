from pwn import *

context.log_level='info'
context.arch='amd64'

p = process("/challenge/embryoasm")
#i=rbx
#n=rsi
assembly = """
loop:
    cmp rbx, rsi
    jge average
    add rax, [rdi]
    add rdi, 8
    inc rbx
    jmp loop
average:
    div rsi
"""
code = asm(assembly)
p.send(code)
p.interactive()
