#include <stdio.h>

extern int my_asm_function(int a, int b);

int main() {
    int result = my_asm_function(5, 3);
    printf("Result: %d\n", result);
    return 0;
}
