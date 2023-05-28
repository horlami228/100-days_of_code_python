PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as guest_names:
    names = guest_names.readlines()

with open("./Input/Letters/starting_letter.txt") as sending_letter:
    letter = sending_letter.read()
    for name in names:
        striped = name.strip()
        new_letter = letter.replace(PLACEHOLDER, striped)
        with open(f"./Output/ReadyToSend/letter_to_{striped}.docx", mode="w") as ready_letter:
            ready_letter.write(new_letter)

