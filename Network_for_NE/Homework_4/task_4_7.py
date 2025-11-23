mac = "AAAA:BBBB:CCCC"
mac_str = bin(int(mac.replace(":", ""), 16))
print(mac_str)
mac_str = int(mac.replace(":", ""), 16)
print(f"{mac_str:b}")
