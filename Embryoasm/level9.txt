asm -c amd64 "or rax, rdi; and rax, 1; xor rax, 1" | ./embryoasm
