from secrets import token_bytes

key = token_bytes(4096)

flag = open('flag.txt', 'rb').read()

ct = bytes(a ^ b for a, b in zip(flag, key))

print("encrypted flag:", ct.hex())
pt = bytes.fromhex(input("enter plaintext (in hex):"))

if len(pt) > 4096:
    print("err: plaintext too large")
    exit()

ct = bytes(a ^ b for a, b in zip(pt, key))

print("encrypted input:", ct.hex())
