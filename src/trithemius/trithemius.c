#include <stdio.h>
#include <ctype.h>

void trithemius(char *text, int encrypt) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            char start = isupper(text[i]) ? 'A' : 'a';
            int shift = encrypt ? i : -i;
            
            // Handle negative results for decryption by adding 26 before modulo
            text[i] = (char)((((text[i] - start) + shift) % 26 + 26) % 26 + start);
        }
    }
}

int main() {
    char message[] = "Hello World";
    
    printf("Original: %s\n", message);
    
    trithemius(message, 1);
    printf("Encrypted: %s\n", message);
    
    trithemius(message, 0);
    printf("Decrypted: %s\n", message);
    
    return 0;
