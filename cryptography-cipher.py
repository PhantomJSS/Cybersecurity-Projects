import string

def encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    
    return encrypted_message

def decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    message = encrypted_message.translate(cipher)

    return message

message = input("Please enter in your choice of message: ")
key = int(input("Please input your choice of key: "))

encrypted_message = encrypt(message, key)
print(f'Encrypted Message: {encrypted_message}')

decrypted_message = decrypt(encrypted_message, key)
print(f'Decrypted Message: {decrypted_message}')