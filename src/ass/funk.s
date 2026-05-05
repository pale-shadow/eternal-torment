.section .text
.global funk

funk:
    /* AArch64 uses x0, x1 for the first two integer arguments */
    /* This adds two integers and returns the result in x0 */
    add x0, x0, x1
    ret
