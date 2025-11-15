#  3/2: print("Hello")
#  3/3: print?
#  3/4: sorted
#  3/5: sorted?
#  3/6: a = 5
#  3/7: b = 2
#  3/8:
# if a > b:
#     print("...")
#  3/9: %hist
# 3/10: str + 2
#  4/1: 5 - 3
#  4/2: print(1, 5 - 3, 3)
#  4/3: print(1, 5 - 3, 3)
#  4/4: a = 5
#  4/5: vlans = [1, 2, 3]
#  4/6: print(5)
#  4/7: print(a)
#  4/8: vlans_list = [1, 2, 3]
#  5/1: 1 + 2
#  5/2: 1.0 + 2
#  6/1: a = 5
#  6/2: b = 10
#  6/3: a == b
#  6/4: 10.0 == 10
#  6/5: c =4.5
#  6/6: type(c)
#  6/7: type(b)
#  6/8: "5"
#  6/9: a = "5"
# 6/10: type(a)
# 6/11: a = int(a)
# 6/12: a
# 6/13: data = "10"
# 6/14: int(data)
# 6/15: int(data, 2)
# 6/16: int("11111111", 2)
# 6/17: int("10000000", 2)
# 6/18: int("11000000", 2)
# 6/19: int("11200000", 2)
# 6/20: int("11100000", 2)
# 6/21: int("11110000", 2)
# 6/22: int("11110000")
# 6/23: int("11110010", 2)
# 6/24: bin(255)
# 6/25: bin(225)
# 6/26: hex(255)
# 6/27: oct(255)
# 6/28: int("0x11",16)
# 6/29: a = bin(225)
# 6/30: a
# 6/31: b = a[2:]
# 6/32: b
# 6/33: h = "ff"
# 6/34: o = int("ff", 16)
# 6/35: o
# 6/36: k = bin(o)
# 6/37: k
# 6/38: h = "ff"
# 6/39: o = bin(int("ff", 16))
# 6/40: o
# 6/41: 10 * 2 + 3
# 6/42: int(4.5)
# 6/43: "Hello"
# 6/44: 'Hello'
# 6/45: """"""
# 6/46: """ Anton """
# 6/47: 'I\'m Anton Shevchuk'
# 6/48: a = "test" "hello"
# 6/49: a
# 6/50: template = ("int tun 0\n" "ip addr 10.10.10.1 255.255.255.0\n" "ip mtu 1416" "ip ospf hello-interval 5\n" "tunnel source FastEthernet1/0\n" "tunnel protection ipsec profile DMVPN\n")
# 6/51: templat
# 6/52: template
# 6/53: template = ("int tun 0\n" " ip addr 10.10.10.1 255.255.255.0\n" " ip mtu 1416" " ip ospf hello-interval 5\n" " tunnel source FastEthernet1/0\n" " tunnel protection ipsec profile DMVPN\n")
# 6/54: template
# 6/55:
# tunnel = """
# int tun 0
# ip addr 10.10.10.1 255.255.255.0
# ip mtu 1416
# ip ospf hello-interval 5
# tunnel source FastEthernet1/0
# tunnel protection ipsec profile DMVPN"
# """
# 6/56: tunnel
# 6/57:
# tunnel = """int tun 0
#  ip addr 10.10.10.1 255.255.255.0
#  ip mtu 1416
#  ip ospf hello-interval 5
#  tunnel source FastEthernet1/0
#  tunnel protection ipsec profile DMVPN"
#  """
# 6/58: tunnel
# 6/59:
# tunnel = """int tun 0
#  ip addr 10.10.10.1 255.255.255.0
#  ip mtu 1416
#  ip ospf hello-interval 5
#  tunnel source FastEthernet1/0
#  tunnel protection ipsec profile DMVPN
#  """
# 6/60: tunnel
# 6/61: print(tunnel)
# 6/62: tunnel
# 6/63: from pprint import pprint
# 6/64: pprint(tunnel)
# 6/65: print(tunnel)
# 6/66: tunnel
# 6/67: cmd = "interface Gi0/0"
# 6/68: cmd[0]
# 6/69: cmd[-1]
# 6/70: cmd[-2]
# 6/71: cmd[-1]
# 6/72: cmd[1]
# 6/73: cmd[0:8]
# 6/74: cmd[:8]
# 6/75: cmd[:-1]
# 6/76: cmd
# 6/77: cmd[::-1]
# 6/78: index = 2
# 6/79: count = 5
# 6/80: cmd[index:count]
# 6/81: cmd[index:index + count]
# 6/82: print?
# 6/83: cmd[:2]
# 6/84: cmd[-7:5]
# 6/85: num = 255
# 6/86: num_dec = bin(num)
# 6/87: num_dec_with_0b = num_dec[2]
# 6/88: num_dec
# 6/89: num_dec_with_0b = num_dec[2:]
# 6/90: num_dec_with_0b
# 6/91: cmd[0] = "I"
# 6/92: cmd
# 6/93: n_cmd = replace?
# 6/94: n_cmd = cmd.replace?
# 6/95: n_cmd = cmd.replace("i", "I")
# 6/96: n_cmd
# 6/97: n_cmd = cmd.?
# 6/98: cmd.?
# 6/99: cmd.
# cmd = "interface Gi0/0"
# cmd.upper()
# cmd
# cmd_up = cmd.upper()
# cmd_up
# cmd
# cmd.lower?
# cmd.count?
# cmd.startswith?
# cmd.startswith("i")
# cmd.endswith("i")
# cmd.endswith?
# cmd.endswith(0)
# cmd.endswith("0")
# cmd.startswith("interface")
# cmd.startswith("Interface")
# if cmd.startswith("Interface"):
#     print("this is interface")
# if cmd.startswith("interface"):
#     print("this is interface")
# if cmd.endswith("0/0"):
#     print("this is interface 0/0")
# if cmd.endswith("0/1"):
#     print("this is interface 0/0")
# cmd.startswith("enterface")
# cmd.startswith("enterface", 1)
# cmd.startswith("enterface", 1)?
# cmd.startswith("enterface"?
# cmd.startswith?
# cmd.startswith("nterface", 1)
# cmd_switchport = " switchport"
# cmd.startswith("switchport", 1)
# cmd_switchport.startswith("switchport", 1)
# cmd_switchport.startswith(("switchport", " switchport"))
# cmd_switchport.startswith(("test", " sw"))
# cmd
# cmd.count?
# cmd.count()
# cmd.count(e)
# cmd.count("e")
# cmd.count("e", 0:4)
# cmd.count("e", [0:4])
# cmd.count("e", "e"[0:4])
# cmd.count("e"[0:4])
# cmd.count("e"[0:3])
# cmd
# cmd.count("e[0:3]")
# cmd.count("e[0:4]")
# cmd.count(e[0:4])
# cmd.count(" ")
# ip = "10.1.1.1"
# ip.count(".")
# ip.find(".")
# ip.find?
# ip.find(?
# ip.find()?
# ip.find("o")
# ip.find("0")
# ip.find("0", 3)
# ip.find("0", 1)
# ip.find("0", 2, 4)
# ip.find("1", 2, 4)
# cmd
# find_word = "erf"
# cmd.find(find_word)
# index = cmd.find(find_word)
# cmd[index:]
# cmd[index:index + len(find_word)]
# cmd.replace("i","I")
# cmd
# cmd_repl = cmd.replace("i","I")
# cmd.replace?
# cmd_repl = cmd.replace("i","I")
# cmd_repl
# cmd_repl = cmd.replace("I","i")
# cmd_repl
# cmd_repl = cmd.replace("i","I",count=1)
# cmd_repl
# cmd_repl = cmd.replace("i","I",count=2)
# cmd_repl
# cmd_repl = cmd.replace("I","i")
# cmd_repl
# cmd_change = cmd.replace("Gi","Fa")
# cmd_change
# cmd.replace("0","1",count=1)
# cmd
# cmd.replace("0","1",count=1)
# ip
# ip.replace?
# ip.replace(".","")
# ip_wout_dot = ip.replace(".","")
# ip_wout_dot
# ip_wout_dot_one = ip.replace(".", "").replace("1", "0")
# ip_wout_dot_one
# cmd = "\n\ninterface Gi0/0\n\t"
# print(cmd)
# cmd
# cmd.strip()
# cmd.strip?
# ad = [110/25]
# ad.strip([)
# ad.strip("[")
# ad.strip("[]")
# ad
# ad = "[110/25]"
# ad.strip("[]")
# ad.strip("[")
# ad.strip("]")
# ad.strip("][")
# ad = "[110/[]25]"
# ad.strip("][")
# cmd
# cmd.lstrip?
# cmd.lstrip()
# cmd.rstrip()
# print(cmd.lstrip())
# print(cmd.rstrip())
# print(cmd)
# cmd
# cmd = " switchport mode access"
# cmd
# cmd.rstrip()
# cmd
# cmd = " switchport mode access\n"
# cmd
# print(cmd)
# cmd.rstrip()
# cmd = " switchport trunk allowed vlan 1,2,3,4,5\n"
# print(cmd)
# cmd.split()
# cmd.replace(",", " ")
# cmd.replace(",", " ").replace("\n","")
# cmd.replace(",", " ").replace("\n","").lstrip().split()
# cmd_vlans = cmd.replace(",", " ").replace("\n","").lstrip().split()
# cmd_vlans
# cmd_vlans[4:]
# cmd_vlans = cmd_vlans[4:]
# cmd_vlans
# cmd
# cmd.split()
# cmd.split()[-1]
# cmd.split()[-1].split(",")
# ip = "10.1.1.1"
# ip.split(".")
# cmd.index?
# cmd.index(".")
# ip.index(".")
# ip.isalnum
# ip.isalnum?
# ip.isalpha
# ip.isalpha?
# ip.isascii?
# ip.decimal?
# ip.isdecimal?
# ip.isdigit
# ip.isdigit?
# ip.rsplit(".")
# ip.split(".")
# cmd = "interface Gi0/{}"
# cmd
# cmd.format(10)
# cmd = "interface Gi0/{}".format(10)
# cmd
# cmd = "interface Gi0/{}".format?
# cmd = "interface Gi0/{}".format("10")
# cmd
# cmd = "interface Gi0/{}".format([1, 2])
# cmd
# tunnel = """
# int tun {}
#  ip addr {}
#  ip mtu 1416
#  ip ospf hello-interval 5
#  tunnel source {}
#  tunnel protection ipsec profile DMVPN
#  """
# tunnel
# tunnel.format(0,10.1.1.1,192.168.1.1)
# tunnel.format(0,"10.1.1.1","192.168.1.1")
# tunnel = tunnel.format(0,"10.1.1.1","192.168.1.1")
# print(tunnel)
# tunnel = tunnel.format(0,"10.1.1.2","192.168.2.1")
# print(tunnel)
# tunnel
# tunnel_template = '\nint tun {}\n ip addr {}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {}\n tunnel protection ipsec profile DMVPN\n '
# tunnel_template
# print(tunnel_template)
# print(tunnel_template.format(0, "192.168.1.1", "10.10.10.1"))
# print(tunnel_template.format(0, "192.168.2.1", "10.10.10.2"))
# print(tunnel_template.format(0, "192.168.2.1 255.255.255.0", "10.10.10.2"))
# print(tunnel_template.format(0, "192.168.1.1 255.255.255.0", "10.10.10.1"))
# tunnel_template = '\nint tun {1}\n ip addr {0}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {2}\n tunnel protection ipsec profile DMVPN\n '
# print(tunnel_template.format("192.168.1.1 255.255.255.0", 0, "10.10.10.1"))
# tunnel_template = '\nint tun {tun_num}\n ip addr {ip_addr}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {tun_ip_intf}\n tunnel protection ipsec profile DMVPN\n '
# print(tunnel_template.format(ip_addr = "192.168.1.1 255.255.255.0", tun_num = 0, tun_ip_intf = "10.10.10.1"))
# tunnel_template = '\nint tun {tun_num}\n description tun {tun_num}\n ip addr {ip_addr}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {tun_ip_intf}\n tunnel protection ipsec profile DMVPN\n '
# tunnel
# tunnel_TEMPLATE
# tunnel_template
# PRINT(tunnel_template)
# PRINT(tunnel_template)
# print(tunnel_template)
# print(tunnel_template).format(tun_num = 0, ip_addr = "192.168.1.1 255.255.255.0", tun_ip_intf = "10.1.1.1")
# print(tunnel_template).format(tun_num = 0, tun_num = 0, ip_addr = "192.168.1.1 255.255.255.0", tun_ip_intf = "10.1.1.1")
# print(tunnel_template).format(tun_num = 0, ip_addr = "192.168.1.1 255.255.255.0", tun_ip_intf = "10.1.1.1")
# print(tunnel_template)
# print(tunnel_template.format(tun_num = 0, ip_addr = "192.168.1.1 255.255.255.0", tun_ip_intf = "10.1.1.1"))
# ip_template = "{} {} {} {}"
# ip_template.format(1, 2, 3, 4)
# ip_template.format([1, 2, 3, 4].split(","))
# output = "{} {} {}"
# output.format("Fa0/1", "10.1.1.1", "255.255.255.0")
# output = "{} {} {}\n" * 2
# output
# print(output)
# print(output.format("Fa0/1", "10.1.1.1", "255.255.255.0","Fa0/15", "192.168.100.100", "255.255.255.0"))
# output = "{:8} {:16} {:16}\n" * 2
# print(output.format("Fa0/1", "10.1.1.1", "255.255.255.0","Fa0/15", "192.168.100.100", "255.255.255.0"))
# output = "{:<8} {:16} {:16}\n" * 2
# print(output.format(1, "10.1.1.1", "255.255.255.0", 2, "192.168.100.100", "255.255.255.0"))
# output = "{:<8} {:>16} {:16}\n" * 2
# print(output.format(1, "10.1.1.1", "255.255.255.0", 2, "192.168.100.100", "255.255.255.0"))
# template = "{} {} {} {}"
# template.format(10, 1, 100, 168)
# template = "{:b} {:b} {:b} {:b}"
# template.format(10, 1, 100, 168)
# template = "{:08b} {:08b} {:08b} {:08b}"
# template.format(10, 1, 100, 168)
# template = "{:8} {:8} {:8} {:8}\n {:08b} {:08b} {:08b} {:08b}"
# template.format(10, 1, 100, 168, 10, 1, 100, 168)
# print(template.format(10, 1, 100, 168, 10, 1, 100, 168))
# template = "{:9} {:9} {:9} {:9}\n {:08b} {:08b} {:08b} {:08b}"
# print(template.format(10, 1, 100, 168, 10, 1, 100, 168))
# template = "{:8} {:8} {:8} {:8}\n {:08b} {:08b} {:08b} {:08b}"
# print(template.format(10, 1, 100, 168, 10, 1, 100, 168))
# template = "{0:9}{1:9}{2:9}{3:9}\n {0:08b} {1:08b} {2:08b} {3:08b}"
# print(template.format(10, 1, 100, 168, 10, 1, 100, 168))
# print(template.format(10, 1, 100, 168))
# template = "{0:<9}{1:<9}{2:<9}{3:<9}\n {0:08b} {1:08b} {2:08b} {3:08b}"
# print(template.format(10, 1, 100, 168))
# template = "{0:<9}{1:<9}{2:<9}{3:<9}\n{0:08b}{1:08b}{2:08b}{3:08b}"
# print(template.format(10, 1, 100, 168))
# template = "{0:<9}{1:<9}{2:<9}{3:<9}\n{0:08b} {1:08b} {2:08b} {3:08b}"
# print(template.format(10, 1, 100, 168))
# print(template.format(192, 168, 1, 1))
# template = "{0:<9.1}{1:<9.1}{2:<9.1}{3:<9.1}\n{0:08.1b} {1:08.1b} {2:08.1b} {3:08.1b}"
# print(template.format(192.12, 168.234, 1.32356, 1.0123))
# template = "{0:<9.1}{1:<9.1}{2:<9.1}{3:<9.1}"
# print(template.format(192.12, 168.234, 1.32356, 1.0123))
# int  = "Gi0/0"
# intf  = "Gi0/0"
# f"interface {intf}"
# cmd = "switchport trunk allowed vlan"
# vlan = "1,2,3,4"
# f"{cmd} {vlan}"
# cmd + " " + vlan
# f"{cmd.upper()} {vlan}"
# f"{cmd.upper()} {vlan.split(",")}"
# oct1, oct2, oct3, oct4 = 192, 100, 1, 150
# f"{oct1:9}{oct2:9}{oct3:9}{oct4:9}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}"
# print(f"{oct1:9}{oct2:9}{oct3:9}{oct4:9}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")
# print(f"{oct1:8}{oct2:8}{oct3:8}{oct4:8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")
# print(f"{oct1:<8}{oct2:<8}{oct3:<8}{oct4:<8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")
# print(f"{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")
# template = "{0:<9.1}{1:<9.1}{2:<9.1}{3:<9.1}\n{0:08.1b} {1:08.1b} {2:08.1b} {3:08.1b}"
# template = "{0:<9}{1:<9}{2:<9}{3:<9}\n{0:08b} {1:08b} {2:08b} {3:08b}"
# print(template.format(192.100.1.150))
# print(template.format(192, 100, 1, 150))
# print(f"{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")
