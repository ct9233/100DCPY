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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    original_indexes = []
    encrypted_indexes = []
    encrypted_text = []
    for letter in original_text:
        original_indexes.append(alphabet.index(letter))
    for index in original_indexes:
        if index + shift_amount < 25:
            encrypted_indexes.append(index + shift_amount)
        else:
            encrypted_indexes.append(index + shift_amount - 26)
    for index in encrypted_indexes:
        encrypted_text.append(alphabet[index])
    print(f"The encrypted output is: {''.join(encrypted_text)}")


encrypt(text, shift)