st = "some text here"  # string
bs = b"some text here"  # byte string
print("some text here type[str] st[0] type[str]:", st[0])
print("b'some text here' type[bytes] bs[0] type[int]:", bs[0])

bs2 = bytes([32, 115, 111, 35, 127, 32, 48])  # b" so#\x7f 0"
print("b'some text here' + b' so#\x7f'", bs + bs2)

# \x7f hexadecimal

# decimal 0123456789
# hexadecimal 0123456789abcdef a = 10, b = 11, c = 12, d = 13, e = 14, f = 15
# binary 1111 1111
#       7654 3210
#       0000 1010 = 10
#       0100 0100 = 68
#     \b0111 1111 = \x7f = d112+15 = d127 # hexadecimal -> binary -> decimal


# 525 = 5*10^2+2*10^1+5*10^0 -> 500 + 20 + 5 = 525 decimal
# \x7f  = 7*16^1+f*16^0 -> 7 * 16 + 15 = 127 hexadecimal to decimal
# \o74  = 7*8^1 + 4*8^0 -> 56+4 = 60 # octal to decimal

with open(
    "text.bin", "wb+"
) as f2:  # b'some text here' + b' so#⌂' b'some text here so#\x7f 0'
    f2.write(bs + bs2)
    f2.seek(0)
    print(f2.read())

with open(
    "text.bin", "r"
) as f3:  # <built-in method read of _io.TextIOWrapper object at 0x000001ED5E5D65E0>
    print(f3.read)
