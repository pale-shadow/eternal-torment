.section .text
.global _start

_start:
    /* Set up test arguments in x0 and x1 */
    mov x0, #5
    mov x1, #10
    
    /* Call your function */
    bl funk

    /* Exit system call (AArch64 exit is 93) */
    mov x0, #0      /* Status 0 */
    mov x8, #93     /* syscall number */
    svc #0          /* Invoke syscall */

.global funk
funk:
    add x0, x0, x1
    ret
