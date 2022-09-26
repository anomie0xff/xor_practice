from secrets import token_bytes

KEY_LEN = 6
key_1 = token_bytes(KEY_LEN)
key_2 = token_bytes(KEY_LEN)

flag = open('flag.txt', 'rb').read()

ct = b''
for i in range(0, len(flag), KEY_LEN):
    temp = bytes(a ^ b for a, b in zip(flag[i:i+KEY_LEN], key_1))
    ct += bytes(a ^ b for a, b in zip(temp, key_2))

print(ct.hex())
