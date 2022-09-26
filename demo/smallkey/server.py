from random import randint

flag = open('flag.txt', 'rb').read()

key = randint(0, 0x100)

ct = b''

for i in flag:
    ct += (key^i).to_bytes(1, byteorder='big')

print(ct.hex())
