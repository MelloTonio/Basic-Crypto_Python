from string import ascii_uppercase as alphabet

letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0,
                'E': 0, 'F': 0, 'G': 0, 'H': 0, 
                'I': 0, 'J': 0, 'K': 0, 'L': 0, 
                'M': 0, 'N': 0, 'O': 0, 'P': 0,
                'Q': 0, 'R': 0, 'S': 0, 'T': 0,
                'U': 0, 'V': 0, 'W': 0, 'X': 0,	
                'Y': 0, 'Z': 0}
            
english_letter_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


file = open('Frequency Analysis\exampleFile.txt','r').read().upper()

for letter in file:
    if letter in alphabet:
        letter_count[letter] += 1

order = []
score = 0

for most_common_letter in sorted(letter_count, key=letter_count.get, reverse=True):
    print(most_common_letter,letter_count[most_common_letter])
    order.append(most_common_letter)

order = ''.join(order)

for top_6_common_letters in english_letter_freq[:6]:
    if top_6_common_letters in order[:6]:
        score += 1

for top_6_uncommon_letters in english_letter_freq[-6:]:
    if top_6_uncommon_letters in order[-6:]:
        score += 1
    

print(f'Score: {score} out of 12')

