ip = "192.168.3.1"
list_ip = ip.split(".")
oct_1 = int(list_ip[0])
oct_2 = int(list_ip[1])
oct_3 = int(list_ip[2])
oct_4 = int(list_ip[3])
print(
    f"{oct_1:<8} {oct_2:<8} {oct_3:<8} {oct_4:<8}\n{oct_1:08b} {oct_2:08b} {oct_3:08b} {oct_4:08b}"
)
# template = "{0:<8} {1:<8} {2:<8} {3:<8}\n{0:08b} {1:08b} {2:08b} {3:08b}"

# print(template.format(oct_1, oct_2, oct_3, oct_4))
