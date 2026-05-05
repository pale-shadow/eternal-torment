def rail_fence_cipher(text, rails, encrypt=True):
    # Create the matrix (fence) filled with placeholders
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    
    # Determine the zigzag pattern
    rail = 0
    direction = 1 # 1 for down, -1 for up
    
    if encrypt:
        # Fill the fence in a zigzag pattern
        for i in range(len(text)):
            fence[rail][i] = text[i]
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        
        # Read the fence row by row
        return "".join([char for row in fence for char in row if char != '\n'])

    else:
        # Decryption logic
        # 1. Mark the zigzag path with '*'
        for i in range(len(text)):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        
        # 2. Fill the marked positions with ciphertext characters
        index = 0
        for r in range(rails):
            for c in range(len(text)):
                if fence[r][c] == '*' and index < len(text):
                    fence[r][c] = text[index]
                    index += 1
        
        # 3. Read the fence in the zigzag pattern to recover plaintext
        result = []
        rail, direction = 0, 1
        for i in range(len(text)):
            result.append(fence[rail][i])
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        
        return "".join(result)

# Practice Test
message = "HELLOWORLD"
num_rails = 3

encrypted = rail_fence_cipher(message, num_rails, encrypt=True)
decrypted = rail_fence_cipher(encrypted, num_rails, encrypt=False)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")