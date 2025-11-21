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
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLAN: "}
vlan = input(question[interface_mode])
dict_template = {"access": access_template, "trunk": trunk_template}
str1 = "\n".join(dict_template[interface_mode])
print(f"\ninterface {interface_type_number}\n{str1.format(vlan)}\n")
