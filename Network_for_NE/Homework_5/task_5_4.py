ip_addr_with_mask = input("\nEnter IP address in format (example: 192.168.1.1/24): ")
ip_addr = ip_addr_with_mask.split("/")[0].split(".")
mask = ip_addr_with_mask.split("/")[1]
print(
    "\nNetwork:\n{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}".format(
        int(ip_addr[0]), int(ip_addr[1]), int(ip_addr[2]), int(ip_addr[3])
    )
)
mask_in_bin = "1" * int(mask) + "0" * (32 - int(mask))
first_octet = int(mask_in_bin[0:8], 2)
second_octet = int(mask_in_bin[8:16], 2)
third_octet = int(mask_in_bin[16:24], 2)
forth_octet = int(mask_in_bin[24:32], 2)
print(
    f"\nMask:\n/{mask}\n"
    "{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}\n".format(
        first_octet, second_octet, third_octet, forth_octet
    )
)
