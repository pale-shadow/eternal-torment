section .text
global funk

funk:
    ; Example function: add two integers
    mov eax, [esp + 4]
    add eax, [esp + 8]
    ret