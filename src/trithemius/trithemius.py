def trithemius_cipher(text, encrypt=True):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            # Determine starting point (A=65, a=97)
            start = ord('A') if char.isupper() else ord('a')
            # Shift increases by the index 'i'
            shift = i if encrypt else -i
            # Calculate new character
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

# Practice Test
message = "Hello World"
encrypted = trithemius_cipher(message)
print(f"Encrypted: {encrypted}")
