import pandas

code_words_df = pandas.read_csv("nato_phonetic_alphabet.csv")
code_words = {row.letter:row.code for (index, row) in code_words_df.iterrows()}

user_word = input("Enter a word to have spelled in the NATO phonetic alphabet: ")

code_reply = [code_words[f"{letter}"] for letter in list(user_word.upper())]

print(code_reply)