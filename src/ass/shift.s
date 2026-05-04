// Trithemius Logic for a single character
// x0 = character to shift
// x1 = current index (the shift value)
// x2 = start char ('A' or 'a')

// 1. Normalize: subtract start ('A' or 'a') to get 0-25 range
sub x0, x0, x2

// 2. Add the shift (the index i)
add x0, x0, x1

// 3. Modular arithmetic (x0 % 26)
// We divide by 26, multiply back, and subtract to find the remainder
mov x3, #26
udiv x4, x0, x3     // x4 = x0 / 26
msub x0, x4, x3, x0 // x0 = x0 - (x4 * 26)

// 4. Denormalize: add start back
add x0, x0, x2
