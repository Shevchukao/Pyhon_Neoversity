str = "Hello shiny World"
# str[2] = "w" #  string does not support item assignment

print("String str: ", str)  # print string str
print("Char with index 1 str[1]: ", str[1])  # print char with index 1 -> "e"
print(
    "Slice with char from 1(included) to 2(excluded) str[1:2]: ", str[1:2]
)  # print slice with char from 1(included) to 2(excluded) -> "e"
print(
    "Copy str to lowercase str.lower(): ", str.lower()
)  # method with copy str(not changed) to lowercase
print(
    "Copy str to uppercase str.upper(): ", str.upper()
)  # method with copy str(not changed) to uppercase

str1 = "hello shiny world"  # string str1
print("String str1: ", str1)  # print string str1 -> hello shiny world
print(
    "First word start with uppercase, other words lowercase, capitalize string str1 str1.capitalize(): ",
    str1.capitalize(),
)  # First word start with uppercase, other words lowercase -> Hello shiny world
print(
    'Split words in list using separator such as " ", "/", "_", ",","." str1.split(" "): ',
    str1.split(" "),
)  # Split words in list using separator such as " ", "/", "_", ",","." -> ['hello', 'shiny', 'world']
print(
    'Split words in list using separator such as char "o" str1.split("o"): ',
    str1.split("o"),
)  # Split words in list using separator such as letter "o" or number "2" -> ['hell', ' shiny w', 'rld']
print(
    'Split words in list using separator such as char "o" and show list with index 2 str1.split("o")[2]: ',
    str1.split("o")[2],
)  # Split words in list using separator such as letter "o" and show list with index 2 -> rld
str2 = str1.split()  # split string with separator
print(
    "Split string str1.split():", str2
)  # print split string with separator " " -> ['hello', 'shiny', 'world']
print(
    "Join list str2 in string: ",
    "_".join(str2),
)  # Join words in list str2 using separator "_" -> hello_shiny_world

str3 = "helloshinyworld"
print('String str3 = "helloshinyworld": ', str3)  # print string str3
str4 = "22helloshinyworld"
print('String str4 = "22helloshinyworld": ', str4)  # print string str4
str5 = "2345"
print('String str5 = "2345": ', str5)  # print string str5
print(
    "Check string, only letter without space and number: ", str3.isalpha()
)  # check string, only letter without space and number -> True
print(
    "Check string, letter and number only without space", str4.isalnum()
)  # check string, letter and number only without space -> True
print(
    "Check string, only number without space", str5.isnumeric()
)  # check string, only integer number(not float) without space -> True
str6 = "_anton"
print('String str6 = "_anton": ', str6)  # print string str6
print(
    'Check string(variable), start from letter or "_":', str6.isidentifier()
)  # Check string(variable), start from letter or "_" -> True
print(
    'Change in string letter "a" to "A":', str6.replace("a", "A")
)  # Change in string letter "a" to "A"

str7 = "Hello"
str8 = f"{str7} world {1+2}"  # f string
print(str8)
