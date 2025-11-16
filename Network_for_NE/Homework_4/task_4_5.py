command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
# command1_vlans = set(command1.split()[-1].split(","))
# command2_vlans = set(command2.split()[-1].split(","))
# result = sorted(list(command1_vlans & command2_vlans))
result = sorted(
    list(set(command1.split()[-1].split(",")) & set(command2.split()[-1].split(",")))
)
print(result)
