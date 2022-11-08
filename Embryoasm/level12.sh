asm -c amd64 "mov rax, 0xdeadbeef00001337; mov rbx, 0xc0ffee0000; mov [rdi], rax; mov [rsi], rbx" | ./embryoasm
