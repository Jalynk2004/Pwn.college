asm -c amd64 "mov rbx, [rdi];mov rcx, [rdi+8];add rbx, rcx; mov [rsi], rbx" | ./embryoasm

