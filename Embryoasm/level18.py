from pwn import *

context.log_level='info'
context.arch='amd64'

p = process ("/challenge/embryoasm")
assembly = """
    cmp dword ptr [rdi], 0x7f454c46
    jne else_1
    jmp right
right:
    mov eax, dword ptr [rdi+4]
    add eax, dword ptr [rdi+8]
    add eax, dword ptr [rdi+12]
    jmp exit
else_1:
    cmp dword ptr [rdi], 0x00005a4d
    jne else
    mov eax, dword ptr [rdi+4]
    sub eax, dword ptr [rdi+8]
    sub eax, dword ptr [rdi+12]
    jmp exit
else:
    mov rax, 1 
    mul dword ptr [rdi+4]
    mul dword ptr [rdi+8]
    mul dword ptr [rdi+12]
    jmp exit
exit:
    nop
"""
code = asm(assembly)
p.send(code)
p.interactive()
