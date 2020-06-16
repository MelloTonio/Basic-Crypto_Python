from string import ascii_lowercase as alphabet

message = str(input("Type the message: "))
key = int(input("Write the key: "))
mode = int(input("DEC[0]/ENC[1]?"))
final_message = ''

for char in message:
    if char in alphabet:
        indexOfLetter = alphabet.find(char)
        if mode == 1:
            # If the sum equals to 26 or more the alphabet will be "reseted"
            indexOfLetter = (indexOfLetter + key) % 26 
        if mode == 0:
            indexOfLetter = (indexOfLetter - key) % 26
        final_message += alphabet[indexOfLetter]
    else:
        final_message += char

print(final_message)