# vlans = [1, 2, 3, 4]
# access = []
# access = ["switchport mode access", "switchport access vlan", "switchport nonegotiate", "spanning-tree portfast", "spanning-tree bpduguard enable"]
# access = ["switchport mode access", \ "switchport access vlan", "switchport nonegotiate", "spanning-tree portfast", "spanning-tree bpduguard enable"]
# access = [
# "switchport mode access",
# "switchport access vlan",
# "switchport nonegotiate",
# "spanning-tree portfast",
# "spanning-tree bpduguard enable"
# ]
# vlan
# vlan.split(",")
# list("test")
# vlans
# vlan[0]
# vlan[1]
# vlans[1]
# vlans[0]
# vlans[0:2]
# vlans[2:]
# vlans[::2]
# vlans[::-1]
# vlans[-1] = 1200
# vlans
# interfaces = [["FastEthernet0/0", "15.0.15.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/1", "10.0.1.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/2", "10.0.2.1", "YES", "manual", "up", "down"],
# interfaces = [["FastEthernet0/0", "15.0.15.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/1", "10.0.1.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/2", "10.0.2.1", "YES", "manual", "up", "down"],]
# interfaces
# interfaces[0]
# interfaces[1]
# interfaces[2]
# interfaces[0][1]
# interfaces[1][-1]
# list0 = interfaces[0]
# list0[1]
# list0_1 = list0[1]
# list0_1[-1]
# interfaces[0][1][-1]
# len(interfaces)
# len(interfaces[0])
# vlans
# len(vlans)
# vlans = [1000, 10, 101, 2, 21, 102]
# sorted(vlan)
# sorted(vlans)
# sorted?
# sorted(vlans, reverse=True)
# vlans
# interfaces[0][-1]
# interfaces
# interfaces[0][-1] = "down"
# interfaces
# interfaces = [["FastEthernet0/1", "15.0.15.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/11", "10.0.1.1", "YES", "manual", "up", "up"],
# ["FastEthernet0/2", "10.0.2.1", "YES", "manual", "up", "down"],]
# sorted(interfaces)
# data = [[1, 100, 1000], [2, 2, 2], [1, 2, 3], [4, 100, 3]]
# sorted(data)
# sorted(data[-1])
# data_text = ["Hello", "hello", "Unix", "Windows"]
# sorted(data_text)
# ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]
# sorted(ip_list)
# vlans
# vlans[3]
# vlans[3] = 21
# vlans
# set(vlans)
# vlans
# vlans.sort()
# vlans
# result = sorted(vlans)
# result
# vlans = [1000, 10, 101, 2, 21, 102]
# result = sorted(vlans)
# result
# vlans
# result.sort()
# vlans.sort()
# vlans
# result = vlans.sort()
# print(result)
# vlans = [1000, 10, 101, 2, 21, 102]
# vlans.count(2)
# vlans.count?
# vlans.insert(3, 21)
# vlans
# vlans.insert?
# vlans.append(202)
# vlans
# vlans.?
# vlans.remove?
# vlans.remove(21)
# vlans
# vlans.insert(3, 21)
# vlans.remove(2)
# vlans
# vlans.copy?
# vlans1 = vlans.copy()
# vlans1
# vlans.copy?
# vlans.extend(vlans1.reverse())
# vlans1.reverse()
# vlans1
# vlans1.reverse?
# vlans2 = vlans1.reverse()
# vlans
# vlans2
# vlans1
# vlans.extend(vlans1)
# vlans
# vlans.index(202)
# vlans.pop?
# vlans.pop()
# vlans
# vlans.pop(index=0)
# vlans.pop(0)
# vlans
# vlans.index?
# vlans.remove?
# vlans1 = vlans.sort()
# vlans1
# vlans
# vlans.append?
# vlans.append()
# vlans.append(202)
# vlans.reverse()
# vlans.sort()
# vlans.copy()
# vlans.clear()
# vlans
# vlans.extend(vlans1)
# vlans2 = vlans.extend(vlans1)
# vlans1
# vlans1 = vlans.sort()
# vlans2 = vlans.extend(vlans1)
# vlans1
# vlans1 = vlans.sort()
# vlans1
# vlans1 = [10, 10, 21, 21, 21, 21, 101, 101, 102, 102, 202, 202, 202]
# lans
# vlans
# vlans2
# vlans = [1000, 10, 101, 2, 21, 102]
# vlans.extend(vlans1)
# vlans1
# vlans
# vlans.append([100, 200])
# vlans
# vlans + vlans1
# vlans
# vlans1
# vlans + vlans1
# all_vlans = vlans + vlans1
# vlans
# vlans1
# vlans_str = ["1", "2", "3"]
# ",".join(vlans_str)
# "|".join(vlans_str)
# " | ".join(vlans_str)
# " | ".join(vlans)
# access
# "\n".join(access)
# print("\n".join(access))
# data_join = "\n".join(access)
# data.split("\n")
# data_join.split("\n")
# data_split = data_join.split("\n")
# data_split
# int?
# a = "101"
# print(a, 2)
# print(int(a, 2))
# print(int(a, 10))
# a = b = c = 500
# id(a) == id(b)
# a = 500
# b = 500
# id(a) == id(b)
# num = 10
# print(hex(num))
# num = 10
# num += 2
# print(num)
# s = "interface"
# print(s[3])
# print(s[:4])
# print(s[:])
# print(s[::2])
# s = "FastEthernet0/1 10.1.1.1 255.255.255.0"
# print(s.split()[-2])
# print(s.split()[-1].split("."))
# f = "Result: {} {}"
# print(f.format(100, 2))
# print(f.format(100, "test"))
# f = "Result: {:b} {}"
# print(f.format(8, 2))
# f = "Result: {:b} {:b}"
# print(f.format(8, 2))
# f = "Result: {:08b} {:08b}"
# print(f.format(8, 2))
# a = "101"
# a = int(a, 2)
# a = 101
# a = int(a, 2)
# a
# list_of_lists = [
# [11, 12, 13, 14, 15, 16],
# [21, 22, 23, 24, 25, 26],
# [31, 32, 33, 34, 35, 36]]
# print(list_of_lists[-2][4])
# print(list_of_lists[-2][-2])
# print(list_of_lists[1][-2])
# print(list_of_lists[1][4])
# print(list_of_lists[4][4])
# list1 = [1,2,3]
# list2 = [4,5,6]
# result = list1.extend(list2)
# print(result)
# result = list1.append(list2)
# print(result)
# result = list1 + list2
# print(result)
# result.clear
# result.clear()
# print(result)
# result = list1 + list2
# print(result)
# liat1.clear()
# list1.clear()
# list1 = [1,2,3]
# list1
# list2
# result = list1 + list2
# print(result)
# list1 = [1,2,3,4,5,6]
# a = list1.remove(2)
# print(a)
# a = list1.pop(2)
# print(a)
# list1 = [1,2,3,4,5,6]
# a = list1.pop(2)
# print(a)
# list1 = [1,2,3,4,5,6]
# a = list1[-3]
# print(a)
# a = list1[2]
# print(a)
# a = list1[-4]
# print(a)
# a = list1.pop(-4)
# print(a)
# d1 = d2 = {1:100, 2:200, 3:300}
# d1[4] = 400
# print(d1)
# print(d2[4])
# d1 = {1:100, 2:200, 3:300}
# keys = d1.keys()
# print(keys)
# d1[4] = 400
# print(keys)
# d1 = {1:100, 2:200, 3:300}
# keys = list(d1.keys())
# print(keys)
# d1[4] = 400
# print(keys)
# d1
# a = 5
# b = a
# id(a)
# id(b)
# vlans = [1, 2, 3]
# vlans2 = vlans
# id(vlans) = id(vlans2)
# id(vlans) == id(vlans2)
# vlans2.append(4)
# vlans2
# vlans
