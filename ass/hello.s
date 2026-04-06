.global _start

.section .data
message:
    .ascii "Hello Whirled\n"
    .set message_len, . - message

.section .text
_start:
    /* Setup for 'write' system call */
    mov x0, #1              // File descriptor 1 (stdout)
    ldr x1, =message        // Pointer to the message
    mov x2, #message_len    // Message length
    mov x8, #64             // AArch64 write(2) system call number
    svc #0                  // Invoke system call

    /* Setup for 'exit' system call */
    mov x0, #0              // Return code 0
    mov x8, #93             // AArch64 exit(2) system call number
    svc #0                  // Invoke system call
