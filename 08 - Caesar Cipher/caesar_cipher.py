alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

from art import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(original_text, shift_amount, encoding_direction):
    original_indexes = []
    transformed_indexes = []
    returned_text = []
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    for letter in original_text:
        if letter in alphabet:
            original_indexes.append(alphabet.index(letter))
        else:
            original_indexes.append(letter)
    for index in original_indexes:
        if type(index) == int:
            if encoding_direction == "encode":
                if index + shift_amount < 25:
                    transformed_indexes.append(index + shift_amount)
                else:
                    transformed_indexes.append(index + shift_amount - 26)
            elif encoding_direction == "decode":
                if index - shift_amount >= 0:
                    transformed_indexes.append(index - shift_amount)
                else:
                    transformed_indexes.append(index - shift_amount + 26)
        else:
            transformed_indexes.append(index)
    for index in transformed_indexes:
        if type(index) == int:
            returned_text.append(alphabet[index])
        else:
            returned_text.append(index)
    print(f"The {encoding_direction}d output is: {''.join(returned_text)}")


caesar(text, shift, direction)