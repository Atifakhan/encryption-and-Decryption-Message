# Caesar Cipher Encryption and Decryption
# Author: Muhammad Atif
# Description: A simple Python program to encrypt and decrypt text using the Caesar Cipher algorithm.

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher.
    
    :param text: The input string to process
    :param shift: The shift value for the cipher
    :param mode: 'encrypt' or 'decrypt'
    :return: The processed string
    """
    result = ""
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Only shift letters
            # Handle uppercase and lowercase separately
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            result += char
    
    return result


# --- Main Program ---
print("===== Caesar Cipher Encryption & Decryption =====")
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))

print("\n--- Results ---")
encrypted_text = caesar_cipher(message, shift_value, mode='encrypt')
print(f"Encrypted Message: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
print(f"Decrypted Message: {decrypted_text}")
