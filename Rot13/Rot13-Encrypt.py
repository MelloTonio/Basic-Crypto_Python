import string

alphabet = string.ascii_lowercase
new_word = ""
indexes = []

def convert(listr):
    for index in range(0,len(listr)):
      if listr[index] != ' ':
        listr[index] = listr[index] + 13

def cutting_13(listr):
  for number in range(0,len(listr)):
    if listr[number] != ' ':
      if listr[number] > 25:
        new_number = listr[number] - 26
        listr[number] = alphabet.index(alphabet[new_number])

def transpile(listr):
  global new_word
  for index in listr:
    if index != ' ':
      letter = alphabet[index]
      new_word += letter
    else:
      new_word += ' '
  print(new_word)


def rot13(message):
    for letter in message:
       if letter != ' ':
           last =  alphabet.index(letter.lower())
           indexes.append(last)
       else:
          indexes.append(' ')
    convert(indexes)
    cutting_13(indexes)
    transpile(indexes)
