section .text
global my_asm_function

my_asm_function:
    ; Example function: add two integers
    mov eax, [esp + 4]
    add eax, [esp + 8]
    ret