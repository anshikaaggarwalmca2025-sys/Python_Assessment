# Program for Caesar Cipher encryption and decryption

# Function for encryption
def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        if char.isalpha():

            ascii_value = ord(char)

            shifted = ascii_value + shift

            # Handle uppercase letters
            if char.isupper():

                if shifted > 90:
                    shifted -= 26

            # Handle lowercase letters
            else:

                if shifted > 122:
                    shifted -= 26

            encrypted_text += chr(shifted)

        else:
            encrypted_text += char

    return encrypted_text


# Function for decryption
def decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        if char.isalpha():

            ascii_value = ord(char)

            shifted = ascii_value - shift

            # Handle uppercase letters
            if char.isupper():

                if shifted < 65:
                    shifted += 26

            # Handle lowercase letters
            else:

                if shifted < 97:
                    shifted += 26

            decrypted_text += chr(shifted)

        else:
            decrypted_text += char

    return decrypted_text


# Input message
message = input("Enter message: ")

# Shift value
shift = 3

# Encrypt message
encrypted_message = encrypt(message, shift)

# Decrypt message
decrypted_message = decrypt(encrypted_message, shift)

# Display results
print("\nEncrypted Message:", encrypted_message)

print("Decrypted Message:", decrypted_message)



#output:
Enter message: HELLO

Encrypted Message: KHOOR
Decrypted Message: HELLO
