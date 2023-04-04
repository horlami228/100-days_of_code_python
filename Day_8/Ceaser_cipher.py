# This program encodes or decodes our encrypted message
def decipher(text_message, shift_num, instructions): # This function attempts to encrypt or decrypt a message
    cipher_text = ''
    if instructions == "encode":
        for letter in text_message:
            if(letter.isalpha() == 0):
                cipher_text += letter
                continue    
            cipher_text += chr((ord(letter) + shift_num - 97) % 26 + 97)
        print("Your encrypted message is: {}".format(cipher_text))
        print("Copy the message\n")
    elif instructions == "decode":
        for letter in text_message:
            if(letter.isalpha() == 0):
                cipher_text += letter
                continue
            cipher_text += chr((ord(letter) - shift_num - 97) % 26 + 97)
        print("Your decrypted message is: {}".format(cipher_text))
        print("Copy the message\n")   

while(True): # keep program running until user decides to terminate i
    instruction = input("Type 'encode' to encrypty message. Type 'decode' to decrypt message:\n")

    if instruction not in ["encode", "decode"]:
        print("Please enter the right instruction\n")
        exit(-1)
    text = input("Enter your message:\n").lower() # Turn message to lower case

    shift_num = int(input("Enter your shift number:\n"))

    # Perform operations based on user intructions
    decipher(text, shift_num, instruction)
    end_program = input("Type 'yes' if you want to continue. Type 'no' to end program: \n\n")
    if(end_program  in ["no", "NO", "No"]):
        print("Goodbye.\n")
        exit(1)