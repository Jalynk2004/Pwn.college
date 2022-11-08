asm -c amd64 "mov rdi, 0x404000; mov rax, [rdi]; mov rsi, [rdi]; add rsi, 0x1337; mov [rdi], rsi" | ./embryoasm 
