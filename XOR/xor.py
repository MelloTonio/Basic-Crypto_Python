import binascii

message = str(input("Type the message: "))
key = str(input("Write the key: "))
mode = int(input("Decrypt -> [0]/ Encrypt -> [1]: "))

key_index = 0
xored = ''

if mode == 0:
    message = binascii.unhexlify(message)

for msgchar in message:
    if mode == 1:
        xored += chr(ord(key[key_index%len(key)]) ^ ord (msgchar))
    elif mode == 0:
        xored += chr(ord(key[key_index%len(key)]) ^ ord (chr(msgchar)))
    key_index += 1

if mode == 1:
    print(binascii.hexlify(str.encode(xored)))
if mode == 0:
    print(xored)