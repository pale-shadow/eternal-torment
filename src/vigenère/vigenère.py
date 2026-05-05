def vigenere_cipher(text, key, encrypt=True):
    result = []
    key = key.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Find the shift value from the current key character
            shift = ord(key[key_index % len(key)]) - ord('A')
            if not encrypt:
                shift = -shift
            
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            
            # Perform modular arithmetic shift
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
            
            # Only increment key index for alphabetic characters
            key_index += 1
        else:
            # Leave symbols and numbers as-is
            result.append(char)
            
    return "".join(result)

# Example Usage
plaintext = "Attacking at Dawn!"
secret_key = "LEMON"

encrypted = vigenere_cipher(plaintext, secret_key, encrypt=True)
decrypted = vigenere_cipher(encrypted, secret_key, encrypt=False)

print(f"Key:       {secret_key}")
print(f"Original:  {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")