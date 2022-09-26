from secrets import token_bytes

KEY_LEN = 6
key = token_bytes(KEY_LEN)

flag = open('flag.txt', 'rb').read()

ct = b''
for i in range(0, len(flag), KEY_LEN):
    ct += bytes(a ^ b for a, b in zip(flag[i:i+KEY_LEN], key))

print(ct.hex())
