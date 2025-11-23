london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

name_device = input("Введите имя устройства: ")
name_device_lower = name_device.lower()
param_for_some_device = tuple(london_co[name_device_lower].keys())
param_device = input(f"Введите имя параметра {param_for_some_device}: ")
print(london_co[name_device_lower].get(param_device.lower(), "Такого параметра нет"))
