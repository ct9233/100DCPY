#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

invited_names = [i[:-1] if "\n" in i else i for i in invited_names]


for name in invited_names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        form_letter = letter.readlines()
    form_letter[0] = form_letter[0].replace("[name]", f"{name}")
    for i in range(len(form_letter)):
        with open(f"./Output/ReadyToSend/{name}_letter.txt", "a") as invite:
            invite.write(form_letter[i])
