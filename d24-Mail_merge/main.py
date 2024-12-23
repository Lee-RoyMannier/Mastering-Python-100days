#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("Input/Names/invited_names.txt","r") as file:
    names_in_file = file.readlines()

for name in names_in_file:
    names.append(name.strip("\n"))

exemple_letter = open("Input/Letters/starting_letter.txt","r").readlines()

for name in names:
    letter = "".join(exemple_letter).replace("[name]", name)

    with open(f"Output/ReadyToSend/{name}_letter.txt","w") as file:
        file.write(letter)