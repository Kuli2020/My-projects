def caesar_cipher(text, shift, encrypt=True):
    result = ""
    # Adjust the shift value for decryption
    if not encrypt:
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabet characters unchanged
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose either 'E' for encrypt or 'D' for decrypt.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
