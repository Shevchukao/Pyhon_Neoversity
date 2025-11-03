s = "Привіт, світе!"

# UTF-8: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82, \xd1\x81\xd0\xb2\xd1\x96\xd1\x82\xd0\xb5!'
utf_text = s.encode()  # encode
print(f"UTF-8: {utf_text}")
# UTF-16:  b'\xff\xfe\x1f\x04@\x048\x042\x04V\x04B\x04,\x00 \x00A\x042\x04V\x04B\x045\x04!\x00'
utf16_text = s.encode("utf-16")
print(f"UTF-16: {utf16_text}")
# UTF-32:  b'\xff\xfe\x00\x00\x1f\x04\x00\x00@\x04\x00\x008\x04\x00\x002\x04\x00\x00V\x04\x00\x00B\x04\x00\x00,\x00\x00\x00 \x00\x00\x00A\x04\x00\x002\x04\x00\x00V\x04\x00\x00B\x04\x00\x005\x04\x00\x00!\x00\x00\x00'
utf32_text = s.encode("utf-32")
print(f"UTF-32: {utf32_text}")
# cp1251:  b'\xcf\xf0\xe8\xe2\xb3\xf2, \xf1\xe2\xb3\xf2\xe5!'
cp1251_text = s.encode("cp1251")
print(f"cp1251: {cp1251_text}")

# all encode type bytes
print(
    "UTF-8:",
    type(utf_text),
    "UTF-16:",
    type(utf16_text),
    "UTF-32:",
    type(utf32_text),
    "cp1251:",
    type(cp1251_text),
)

with open("test2.bin", "wb") as f:
    f.writelines([utf_text, utf16_text, utf32_text, cp1251_text])

with open("test2.bin", "r") as f:
    print(f.readlines())

restored = utf32_text.decode("utf-32")  # decode utf-32 format
print(restored)
