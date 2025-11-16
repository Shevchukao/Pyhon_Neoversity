mac = "AAAA:BBBB:CCCC"
mac_str = int(mac.replace(":", ""), 16)
print(f"{mac_str:b}")
