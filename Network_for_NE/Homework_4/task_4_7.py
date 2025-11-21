mac = "AAAA:BBBB:CCCC"
mac_str = bin(int(mac.replace(":", ""), 16))
print(mac_str)
# print(f"{mac_str:b}")
