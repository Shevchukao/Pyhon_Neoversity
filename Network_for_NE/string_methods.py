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

# string_methods.py
# Демонстрация работы со строками в Python с подробными комментариями

# ===== БАЗОВЫЕ ОПЕРАЦИИ =====

# Вывод строки "Hello" в консоль
print("Hello")  # Вывод: Hello

# Присвоение значений переменным
a = 5  # Создается переменная a со значением 5
b = 2  # Создается переменная b со значением 2

# Условный оператор - проверяет, больше ли a чем b
if a > b:
    print("...")  # Выполнится, т.к. 5 > 2, вывод: ...

# Арифметические операции
result = 5 - 3  # Результат: 2
print(1, 5 - 3, 3)  # Вывод трех значений: 1 2 3

# Создание переменных разных типов
a = 5  # Целое число
vlans = [1, 2, 3]  # Список чисел
print(5)  # Вывод числа: 5
print(a)  # Вывод переменной a: 5
vlans_list = [1, 2, 3]  # Еще один список

# Операции с числами разных типов
print(1 + 2)  # Сложение целых: 3
print(1.0 + 2)  # Сложение float и int: 3.0

# ===== ОПЕРАЦИИ СРАВНЕНИЯ И ТИПЫ ДАННЫХ =====

a = 5
b = 10
print(a == b)  # Сравнение: False (5 не равно 10)
print(10.0 == 10)  # Сравнение разных типов: True (значения равны)

c = 4.5
print(type(c))  # Тип переменной c: <class 'float'>
print(type(b))  # Тип переменной b: <class 'int'>

# Работа со строками и преобразование типов
text = "5"
print(type(text))  # Тип: <class 'str'>

# Преобразование строки в число
number = int(text)  # Конвертация "5" в 5
print(number)  # Вывод: 5

# Преобразование между системами счисления
data = "10"
print(int(data))  # Десятичное: 10
print(int(data, 2))  # Двоичное: 2 (так как 10 в двоичной = 2 в десятичной)
print(int("11111111", 2))  # 255 (11111111 в двоичной = 255 в десятичной)
print(int("10000000", 2))  # 128
print(int("11000000", 2))  # 192

# Преобразование чисел в разные системы счисления
print(bin(255))  # В двоичную: '0b11111111'
print(bin(225))  # '0b11100001'
print(hex(255))  # В шестнадцатеричную: '0xff'
print(oct(255))  # В восьмеричную: '0o377'

# Обратные преобразования
print(int("0x11", 16))  # Из hex в int: 17

# Работа с двоичными строками
binary_repr = bin(225)  # '0b11100001'
binary_without_prefix = binary_repr[2:]  # Обрезка префикса '0b'
print(binary_without_prefix)  # '11100001'

# Цепочка преобразований: hex -> int -> bin
hex_string = "ff"
decimal_value = int("ff", 16)  # 255
binary_result = bin(decimal_value)  # '0b11111111'
print(binary_result)

# Компактная запись преобразований
print(bin(int("ff", 16)))  # '0b11111111'

# ===== СТРОКОВЫЕ ЛИТЕРАЛЫ И ФОРМАТИРОВАНИЕ =====

# Разные способы создания строк
print("Hello")  # Двойные кавычки
print("Hello")  # Одинарные кавычки
print(""" Anton """)  # Многострочные строки (тройные кавычки)
print("I'm Anton Shevchuk")  # Экранирование апострофа

# Конкатенация строк без оператора +
concatenated = "test" "hello"
print(concatenated)  # 'testhello'

# Создание шаблонов конфигурации для сетевых устройств
template = (
    "int tun 0\n"
    "ip addr 10.10.10.1 255.255.255.0\n"
    "ip mtu 1416"
    "ip ospf hello-interval 5\n"
    "tunnel source FastEthernet1/0\n"
    "tunnel protection ipsec profile DMVPN\n"
)
print(template)

# Улучшенный шаблон с отступами
template = (
    "int tun 0\n"
    " ip addr 10.10.10.1 255.255.255.0\n"
    " ip mtu 1416"
    " ip ospf hello-interval 5\n"
    " tunnel source FastEthernet1/0\n"
    " tunnel protection ipsec profile DMVPN\n"
)
print(template)

# Использование тройных кавычек для многострочных строк
tunnel_config = """
int tun 0
ip addr 10.10.10.1 255.255.255.0
ip mtu 1416
ip ospf hello-interval 5
tunnel source FastEthernet1/0
tunnel protection ipsec profile DMVPN
"""
print(tunnel_config)

# Импорт и использование pprint для красивого вывода
from pprint import pprint

pprint(tunnel_config)  # Форматированный вывод с сохранением структуры

# ===== ОПЕРАЦИИ СО СТРОКАМИ: ИНДЕКСАЦИЯ И СРЕЗЫ =====

cmd = "interface Gi0/0"
print(cmd[0])  # Первый символ: 'i'
print(cmd[-1])  # Последний символ: '0'
print(cmd[-2])  # Предпоследний символ: '/'
print(cmd[1])  # Второй символ: 'n'

# Срезы строк
print(cmd[0:8])  # Символы с 0 по 7: 'interfac'
print(cmd[:8])  # С начала до 7: 'interfac'
print(cmd[:-1])  # Все кроме последнего: 'interface Gi0/'
print(cmd[::-1])  # Реверс строки: '0/0iG ecafretni'

# Срезы с переменными
index = 2
count = 5
print(cmd[index:count])  # 'terf'
print(cmd[index : index + count])  # 'terfac'

# Особые случаи срезов
print(cmd[:2])  # Первые 2 символа: 'in'
print(cmd[-7:5])  # Пустая строка (некорректный диапазон)

# ===== МЕТОДЫ СТРОК =====

# Метод replace() - замена подстрок
original_cmd = "interface Gi0/0"
replaced = original_cmd.replace("i", "I")
print(replaced)  # 'Interface GI0/0'

# Методы изменения регистра
print(original_cmd.upper())  # 'INTERFACE GI0/0'
uppercase_cmd = original_cmd.upper()
print(uppercase_cmd)

# Проверки начала и конца строки
print(original_cmd.startswith("i"))  # True
print(original_cmd.endswith("i"))  # False
print(original_cmd.endswith("0"))  # True
print(original_cmd.startswith("interface"))  # True
print(original_cmd.startswith("Interface"))  # False

# Использование в условных операторах
if original_cmd.startswith("interface"):
    print("this is interface")  # Выполнится

if original_cmd.endswith("0/0"):
    print("this is interface 0/0")  # Выполнится

# Поиск с указанием позиции начала
print(original_cmd.startswith("nterface", 1))  # True (проверка со смещением)

# Проверка начала строки с кортежем вариантов
cmd_switchport = " switchport"
print(cmd_switchport.startswith(("switchport", " switchport")))  # True

# Метод count() - подсчет вхождений
print(original_cmd.count("e"))  # Количество 'e': 2
print(original_cmd.count(" "))  # Количество пробелов: 1

# Для IP-адресов
ip = "10.1.1.1"
print(ip.count("."))  # Количество точек: 3

# Метод find() - поиск позиции подстроки
print(ip.find("."))  # Первая точка на позиции: 2
print(ip.find("o"))  # -1 (не найдено)
print(ip.find("0"))  # 3 (первый '0')
print(ip.find("0", 3))  # 3 (поиск с позиции 3)
print(ip.find("0", 2, 4))  # 3 (поиск в диапазоне [2:4])

# Поиск и извлечение подстроки
find_word = "erf"
position = original_cmd.find(find_word)  # Позиция: 3
print(original_cmd[position:])  # Срез от найденной позиции: 'erface Gi0/0'
print(original_cmd[position : position + len(find_word)])  # Найденная подстрока: 'erf'

# Replace с ограничением количества замен
print(original_cmd.replace("i", "I", 1))  # Замена только первого 'i': 'Interface Gi0/0'
print(original_cmd.replace("i", "I", 2))  # Замена первых двух 'i': 'Interface GI0/0'

# Замена подстрок
print(original_cmd.replace("Gi", "Fa"))  # 'interface Fa0/0'

# Цепочка замен для IP-адреса
ip = "10.1.1.1"
ip_no_dots = ip.replace(".", "")  # Удаление точек: '10111'
ip_modified = ip.replace(".", "").replace("1", "0")  # Цепочка замен: '00000'
print(ip_modified)

# ===== ОБРАБОТКА ПРОБЕЛЬНЫХ СИМВОЛОВ =====

# Методы для работы с пробелами
cmd_with_spaces = "\n\ninterface Gi0/0\n\t"
print("Original:", repr(cmd_with_spaces))
print("strip():", repr(cmd_with_spaces.strip()))  # Удаление с обоих концов
print("lstrip():", repr(cmd_with_spaces.lstrip()))  # Удаление слева
print("rstrip():", repr(cmd_with_spaces.rstrip()))  # Удаление справа

# Обработка сетевых команд
cmd = " switchport trunk allowed vlan 1,2,3,4,5\n"
print("Original command:", repr(cmd))

# Разбиение команды на части
split_cmd = cmd.split()
print(
    "After split():", split_cmd
)  # ['switchport', 'trunk', 'allowed', 'vlan', '1,2,3,4,5']

# Извлечение VLANов
vlans_str = cmd.split()[-1]  # Последний элемент: '1,2,3,4,5'
vlans_list = vlans_str.split(",")  # Разбиение по запятым: ['1','2','3','4','5']
print("VLANs list:", vlans_list)

# Альтернативный способ обработки
processed = cmd.replace(",", " ").replace("\n", "").lstrip().split()
vlans_alt = processed[4:]  # VLANы начиная с 5-го элемента
print("Alternative VLANs extraction:", vlans_alt)

# Разбиение IP-адреса
ip = "10.1.1.1"
octets = ip.split(".")  # Разбиение по точкам: ['10','1','1','1']
print("IP octets:", octets)

# Метод index() - поиск с генерацией исключения
print(ip.index("."))  # Позиция первой точки: 2

# Альтернативные методы разбиения
print(ip.rsplit("."))  # Разбиение справа (аналогично split): ['10','1','1','1']

# ===== ФОРМАТИРОВАНИЕ СТРОК =====

# Базовое форматирование с методом format()
template = "interface Gi0/{}"
formatted = template.format(10)
print(formatted)  # 'interface Gi0/10'

# Форматирование разных типов данных
print("interface Gi0/{}".format("10"))  # Со строкой: 'interface Gi0/10'
print("interface Gi0/{}".format([1, 2]))  # С списком: 'interface Gi0/[1, 2]'

# Многострочные шаблоны
tunnel_template = """
int tun {}
 ip addr {}
 ip mtu 1416
 ip ospf hello-interval 5
 tunnel source {}
 tunnel protection ipsec profile DMVPN
"""
configured_tunnel = tunnel_template.format(0, "10.1.1.1", "192.168.1.1")
print(configured_tunnel)

# Нумерованные плейсхолдеры
template_num = "\nint tun {1}\n ip addr {0}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {2}\n tunnel protection ipsec profile DMVPN\n"
print(template_num.format("192.168.1.1 255.255.255.0", 0, "10.10.10.1"))

# Именованные плейсхолдеры
template_named = "\nint tun {tun_num}\n ip addr {ip_addr}\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source {tun_ip_intf}\n tunnel protection ipsec profile DMVPN\n"
print(
    template_named.format(
        ip_addr="192.168.1.1 255.255.255.0", tun_num=0, tun_ip_intf="10.10.10.1"
    )
)

# Форматирование с выравниванием
output_template = "{:<8} {:16} {:16}\n" * 2
formatted_output = output_template.format(
    1, "10.1.1.1", "255.255.255.0", 2, "192.168.100.100", "255.255.255.0"
)
print("Formatted network config:")
print(formatted_output)

# Форматирование чисел в разных системах счисления
print("Decimal and binary representation:")
template_bin = "{:8} {:8} {:8} {:8}\n {:08b} {:08b} {:08b} {:08b}"
print(template_bin.format(10, 1, 100, 168, 10, 1, 100, 168))

# Использование нумерованных плейсхолдеров для повторного использования
template_reuse = "{0:<8} {1:<8} {2:<8} {3:<8}\n{0:08b} {1:08b} {2:08b} {3:08b}"
print(template_reuse.format(192, 168, 1, 1))

# ===== F-СТРОКИ (СОВРЕМЕННЫЙ ПОДХОД) =====

# Базовые f-строки
interface = "Gi0/0"
fstring_result = f"interface {interface}"
print(fstring_result)  # 'interface Gi0/0'

# F-строки с методами
cmd = "switchport trunk allowed vlan"
vlans = "1,2,3,4"
print(f"{cmd} {vlans}")  # Конкатенация
print(f"{cmd.upper()} {vlans}")  # С преобразованием регистра
print(f"{cmd.upper()} {vlans.split(',')}")  # С вызовом метода

# Форматирование чисел в f-строках
oct1, oct2, oct3, oct4 = 192, 168, 1, 1
binary_table = f"{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}"
print("IP address in decimal and binary:")
print(binary_table)

# Сравнение методов format и f-строк
traditional = "{0:<8} {1:<8} {2:<8} {3:<8}\n{0:08b} {1:08b} {2:08b} {3:08b}".format(
    192, 168, 1, 1
)
modern = f"{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}"

print("Traditional format:")
print(traditional)
print("Modern f-string:")
print(modern)

# Форматирование дробных чисел
template_float = "{0:<9.1f} {1:<9.1f} {2:<9.1f} {3:<9.1f}"
print(template_float.format(192.12, 168.234, 1.32356, 1.0123))
# Вывод: '192.1     168.2     1.3       1.0      '


print("a" > "A")
print(ord("a"))
print(ord("A"))

# Способ 1: Одиночная строка с явными символами новой строки (\n)
# Компактный способ, но менее читаемый для многострочного контента
text = "interface Tunnel10\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416"

print(text)

# Способ 2: Многострочная строка с тройными кавычек
# Более читаемый, но добавляет пустую строку в начале и конце
text2 = """
interface Tunnel10
 ip address 10.10.10.1 255.255.255.0
 ip mtu 1416
"""

print(text2)

# Способ 3: Конкатенация строк в круглых скобках
# Сохраняет читаемость без лишних пустых строк, явно показывает структуру
text3 = (
    "interface Tunnel10\n"
    " ip address 10.10.10.1 255.255.255.0\n"
    " ip mtu 1416        "
)

print(text3)

# Сравнение выводов:
# - text: компактный вывод без лишних отступов
# - text2: появляются лишние пустые строки из-за формата записи
# - text3: чистый вывод, идентичный первому способу

# Рекомендации:
# - Для коротких текстов: способ 1
# - Для конфигураций: способ 3 (лучшая читаемость)
# - Для документации: способ 2 (если убрать переносы после кавычек)
