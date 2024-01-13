from tkinter import *
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
    output_label.config(text=end_text)


window = Tk()
window.title("Caesar Cipher")
window.config(padx=100, pady=20)

title_label = Label(text="Caesar Cipher")
title_label.grid(row=0, column=0, columnspan=2, pady=30)

entry_label = Label(text="Write your input here")
entry_label.grid(row=1, column=0, columnspan=2)

entry = Entry()
entry.grid(row=2, column=0, columnspan=2)

pad_label = Label()
pad_label.grid(row=3, column=0, pady=10)

spinbox_label = Label(text="Choose the shift number")
spinbox_label.grid(row=4, column=0, columnspan=2)

spinbox = Spinbox(from_=0, to=999, width=5)
spinbox.grid(row=5, column=0, columnspan=2)


def encode_button_pressed():
    caesar(entry.get(), int(spinbox.get()), 'encode')


def decode_button_pressed():
    caesar(entry.get(), int(spinbox.get()), 'decode')


encode_button = Button(text="Encode", command=encode_button_pressed)
encode_button.grid(row=6, column=0, pady=30)

decode_button = Button(text="Decode", command=decode_button_pressed)
decode_button.grid(row=6, column=1, pady=30)

output_label = Label()
output_label.grid(row=7, column=0, columnspan=2)

window.mainloop()
