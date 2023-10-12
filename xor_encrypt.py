def xor_encrypt(text, key):
    # Ensure the key is repeated to match the length of the text
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    
    # Perform XOR operation
    encrypted_text = ''.join(chr(ord(text[i]) ^ ord(key[i])) for i in range(len(text)))
    
    return encrypted_text

def xor_decrypt(encrypted_text, key):
    # Ensure the key is repeated to match the length of the encrypted text
    key = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]
    
    # Perform XOR operation
    decrypted_text = ''.join(chr(ord(encrypted_text[i]) ^ ord(key[i])) for i in range(len(encrypted_text)))
    
    return decrypted_text

# Example usage
plaintext = input('enter your plaintext: ')
key = input('enter your key: ')

# Encrypt the plaintext
encrypted_text = xor_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = xor_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)