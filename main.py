alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != 'encode' and direction != 'decode':
    exit(f'Unknown command {direction}.\nAborting.')
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encoded_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        encoded_text += alphabet[new_position]
    print(f"The encoded text is {encoded_text}")

def decrypt(plain_text, shift_amount):
    decoded_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position += len(alphabet)
        decoded_text += alphabet[new_position]
    print(f"The decoded text is {decoded_text}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)