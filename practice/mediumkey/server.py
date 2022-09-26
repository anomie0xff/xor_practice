from secrets import token_bytes

flag = open('flag.txt', 'rb').read()

key = token_bytes(2)

ct = b''

for i in range(0, len(flag), 2):
    ct += bytes(a ^ b for a, b in zip(flag[i:i+2], key))

print(ct.hex())
