ip_addr_with_mask = input("\nEnter IP address in format (example: 192.168.1.1/24): ")
ip_addr = ip_addr_with_mask.split("/")[0].split(".")
ip_addr_bin = f"{int(ip_addr[0]):08b}{int(ip_addr[1]):08b}{int(ip_addr[2]):08b}{int(ip_addr[3]):08b}"
mask = int(ip_addr_with_mask.split("/")[1])
network_address = ip_addr_bin[:mask] + "0" * (32 - mask)
mask_in_bin = "1" * mask + "0" * (32 - mask)

print(
    "\nNetwork:\n"
    "{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}\n".format(
        int(network_address[0:8], 2),
        int(network_address[8:16], 2),
        int(network_address[16:24], 2),
        int(network_address[24:32], 2),
    ),
    f"\nMask:\n/{mask}\n"
    "{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}\n".format(
        int(mask_in_bin[0:8], 2),
        int(mask_in_bin[8:16], 2),
        int(mask_in_bin[16:24], 2),
        int(mask_in_bin[24:32], 2),
    ),
)
