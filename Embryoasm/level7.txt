asm -c amd64 "mov rcx, rdi; shr rcx, 32; mov al, cl" | ./embryoasm
