# london = {"name": "London1", "location": "London Str", "vendor": "Cisco"}
# london[0]
# london["name"]
# london["vendor"]
# value_vendor = london["vendor"]
# london["vendor"] = "Cisco IOS"
# london
# london["IP"] = "10.1.1.1"
# london
# from pprint import pprint
# {"R1": {"hostname": "London_R1",
# "vendor": "Cisco",
# "IP": "10.255.0.1"}
# "R1": {"hostname": "London_R1",
#     ...: "vendor": "Cisco",
# {"R1": {"hostname": "London_R1",
# "vendor": "Cisco",
# "IP": "10.255.0.1"}
# "R1": {"hostname": "London_R1",
# {"R1": {"hostname": "London_R1",
# "vendor": "Cisco",
# "IP": "10.255.0.1"}
# "R2": {"hostname": "London_R1",
# {"R1":{"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.1"}
# "R2": {"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.2"}
# london_co = {"R1":{"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.1"}
#     ...: "R2": {"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.2"}
# london_co = {"R1":{"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.1"}
#     ...: "R2": {"hostname": "London_R1","vendor": "Cisco","IP": "10.255.0.2"}
# london_co = {"R1":{"hostname":"London_R1", "vendor":"Cisco", "IP":"10.255.0.1"},
# "R2":{"hostname":"London_R2", "vendor":"Cisco", "IP":"10.255.0.2"},
# "SW1":{"hostname":"London_SW1", "vendor":"Cisco", "IP":"10.255.0.101"}}
# print(london_co)
# pprint(london_co)
# london_co = {
# "R1":
# {"hostname":"London_R1",
# "vendor":"Cisco",
# "IP":"10.255.0.1"},
# "R2":
# {"hostname":"London_R2",
# "vendor":"Cisco",
# "IP":"10.255.0.2"},
# "SW1":
# {"hostname":"London_SW1",
# "vendor":"Cisco",
# "IP":"10.255.0.101"}}
# pprint(london_co)
# london_co[R2]
# london_co["R2"]
# london_co["R2"]["IP"]
# london_co["SW1"]["vendor"]
# london_co["SW1"]["vendor"] = "HP"
# london_co
# len(london_co)
# sorted(london_co)
# sorted(london_co["SW1"])
# london
# del london["location"]
# london
# london.copy()
# london.fromkeys?
# london.get("IP")
# london.get("I")
# london.get("IP")
# london.update?
# london.update("vpn": None)
# london["vpn"] = None
# london
# london["vpn"]
# london.get("vp", "no key")
# london.get("vp", False)
# "vpn" in london
# "vp" in london
# london.items()
# london.values()
# london.keys()
# keys = london.keys()
# london["locations"] = "London"
# london
# keys
# keys[0]
# london
# keys =list(london.keys())
# keys
# keys[0]
# keys =list(london.items())
# keys
# keys
# keys[0]
# london
# london_update = {"ip":"10.1.1.5", "vendor":"Cisco IOS"}
# london.update(london_update)
# london
# london.pop?
# london.pop("I", "No IP")
# london.pop("IP", "No IP")
# london
# london.popitem?
# london
# london.popitem("vpn")
# london.popitem()
# london
# london.setdefault?
# access = ["sw mode access", "sw access vlan !0", "sw port-security"]
# trunk = ["sw mode trunk", "sw trunk allowed vlan 10,20",]
# access = ["sw mode access", "sw access vlan 1\0", "sw port-security"]
# access = ["sw mode access", "sw access vlan 10", "sw port-security"]
# access
# trunk
# sw_command = {"access": access, "trunk": trunk}
# sw_command
# sw_command["äccess"]
# sw_command["access"]
# access
# access.append("descrition ...")
# access
# sw_command
# d = {1: [1, 2, 2]}
# d[1]
# d[1].append(5)
# d
# d[1].append(5)[0]
# all_vlans = {"sw1": 0, "sw2": 0}
# sw1 = [1, 2, 3, 4]
# sw2 = [2, 3, 4]
# hostnames = ["sw1", "sw2"]
# all_vlans = dict.fromkeys(hostnames)
# all_vlans
# all_vlans = dict.fromkeys(hostnames, 0)
# all_vlans
# all_vlans["sw1"] += 4
# all_vlans["sw2"] += 3
# all_vlans
# all_vlans["sw1"] += len(sw1)
# all_vlans["sw2"] += len(sw2)
# all_vlans
# all_vlans = dict.fromkeys(hostnames, 0)
# all_vlans
# all_vlans["sw1"] += len(sw1)
# all_vlans["sw2"] += len(sw2)
# all_vlans
# all_vlans["sw1"] = all_vlans["sw1"] + len(sw1)
# all_vlans["sw2"] = all_vlans["sw2"] + len(sw2)
# all_vlans
