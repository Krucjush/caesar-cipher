import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
            if new_position < 0:
                new_position += len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += character
    print(f"Here's the {cipher_direction}d result: {end_text}")

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        exit(f'Unknown command {direction}.\nAborting.')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    
    caesar(text, shift, direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if go_again == 'no':
        run = False
        print("Goodbye")