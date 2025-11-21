access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

interface_mode = input("\nВведите режим работы интерфейса (access/trunk): ")
interface_type_number = input("Введите тип и номер интерфейса: ")
vlan = input("Введите номер влан(ов): ")

dict_template = {"access": access_template, "trunk": trunk_template}
str1 = dict_template[interface_mode]
str2 = "\n".join(str1)
print(f"\ninterface {interface_type_number}\n{str2.format(vlan)}\n")
