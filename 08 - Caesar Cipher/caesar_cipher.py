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
    print(f"The encoded output is: {''.join(encrypted_text)}")


def decrypt(encrypted_text, shift_amount):
    encrypted_indexes = []
    decrypted_indexes = []
    decrypted_text = []
    for letter in encrypted_text:
        encrypted_indexes.append(alphabet.index(letter))
    for index in encrypted_indexes:
        if index - shift_amount > 0:
            decrypted_indexes.append(index - shift_amount)
        else:
            decrypted_indexes.append(index - shift_amount + 26)
    for index in decrypted_indexes:
        decrypted_text.append(alphabet[index])
    print(f"The decoded output is: {''.join(decrypted_text)}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
