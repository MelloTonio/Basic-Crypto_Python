from string import ascii_lowercase as alphabet

message = str(input("Type the message: "))
key = str(input("Write the key: "))
mode = int(input("Decrypt -> [0]/ Encrypt -> [1]?"))

middle_key = ''
final_message = ''
letter_reset = 0

for char in message:
    if letter_reset == len(key):
        letter_reset = 0
    if char.lower() in alphabet:
        middle_key += key[letter_reset]
        letter_reset += 1
    else:
        middle_key += char

for char in range(0, len(message)):
    if message[char] in alphabet:
        indexOfLetter_message = alphabet.find(message[char])
        indexOfLetter_middle_key = alphabet.find(middle_key[char])
        if mode == 1:
            indexOfLetter_enc = (indexOfLetter_message +
                                 indexOfLetter_middle_key)
        if mode == 0:
            indexOfLetter_enc = (indexOfLetter_message -
                                 indexOfLetter_middle_key)
        final_message += alphabet[indexOfLetter_enc % 26]
    else:
        final_message += message[char]

print(f'The final message is "{final_message}"')

