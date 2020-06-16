from string import ascii_lowercase as alphabet

message = str(input("Type the message: "))
print("Entering decryption mode...")
final_message = ''


for key in range(1,26):
    for char in message:
        if char in alphabet:
            indexOfLetter = alphabet.find(char)
            indexOfLetter = (indexOfLetter - key) % 26
            final_message += alphabet[indexOfLetter]
        else:
            final_message += char
    print(final_message)
    makeSense = int(input("Does the printed message make sense? Y[0] - N[1]"))
    if makeSense == 0:
        final_key = key
        break
    if makeSense == 1:
        final_message = ''
        continue
print(f'The message decoded by bruteforce was: {final_message} and the key was > {final_key} <')


