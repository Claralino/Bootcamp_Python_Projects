
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser (start_text, shift_amount, direction_chosen):
    end_text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if direction_chosen == 'encode':
            new_position = position + shift_amount
        elif direction_chosen == 'decode':
            new_position = position - shift_amount
        else: 
            print("invalid direction")
        end_text += alphabet[new_position]
    print(f'the {direction_chosen} code is {end_text}')

caeser(text, shift, direction)
