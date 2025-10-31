s = "Hello shiny world!"
start = s.find("l") + 1  # first position element "l" and insert in var start + 1
print(
    "find first position element l .find:", s.find("l")
)  # find first position element "l" -> 2, if not found output -1
print(
    "find second position element l with .find with start:", s.find("l", start)
)  # find second position element "l" -> 3, if not found output -1
start = s.find("l", start) + 1  # second position element "l" and insert in var start
print(
    "find third position element l .find with start:", s.find("l", start)
)  # find third position element "l" -> 15, if not found output -1
print(
    "find last position element l .rfind:", s.rfind("l")
)  # find last position element r(reverse/right) -> 15,, if not found output -1
print("count letter l .count:", s.count("l"))  # count letter "l" in var s -> 3
print("count letters lo .count", s.count("lo"))  # count letter "l0" in var s -> 1
print(
    "index first position element l .index:", s.index("l")
)  # index first position element "l" -> 2, if not found output ValueError
print(
    "index second position element l .index:", s.index("l", 3)
)  # index second position element "l" using start = 3 -> 3, if not found output ValueError

# print("index first position element x .index:", s.index("x"))  # index first position element "x" we can have problem with ValueError need use try: except Exception as e: print(e) or print(Not Found or -1)
# print("index first position element x .rindex:", s.rindex("x"))  # index first position element "x" we can have problem with ValueError need use try: except Exception as e: print(e) or print(Not Found or -1)

print(
    "create list from string using sep = space by default .split: ", s.split()
)  # create list from string using sep = " " or other such as ["l", "_", "/", ".", ","]  by default: ", s.split())
input = "Anton Shevchuk anton.shevchuk.1998@gmail.com (+380)-99-342-50-56"
l1 = input.split()  # split string input using space and insert into list
print("list from string input input.split():", l1)  # list from string input
csv_line = ",".join(
    l1
)  # comma-separated values string from list(method string separator before join)
print("Generate CSV format line using ','.join(l1):", csv_line)

""" CSV File format
first_name,second_name,email,phone
Anton,Shevchuk,anton.shevchuk.1998@gmail.com,+380993425056
Olena,Shevchuk,elena.shevchuk.1966@gmail.com,+380958312101
...
"""
# formate from csv to tsv tab-separated values
input_1 = """Anton,Shevchuk,anton.shevchuk.1998@gmail.com,+380993425056
Olena,Shevchuk,elena.shevchuk.1966@gmail.com,+380958312101"""
input_2 = input_1.split(
    "\n"
)  # deviding by two row using new line delimeter "\n", create list from two element
print("TSV File format:")  # print down TSV file format
for inp in input_2:  # for loop
    inp = inp.split(",")  # split using ","
    print("\t".join(inp))  # join using tab "\t"

""" TSV File format
first_name,second_name,email,phone
Anton   Shevchuk        anton.shevchuk.1998@gmail.com   +380993425056
Olena   Shevchuk        elena.shevchuk.1966@gmail.com   +380958312101
"""

s = "   some nice text    "  # string with spaces
l1 = [
    "    John    ",
    "    Smith    ",
    "    coolmail@mail.com    ",
    "    +34345456565    ",
]  # list with spaces
l2 = []
print(
    "string without some not needed spaces s.strip():", "|", s.strip(), "|"
)  # string without some not needed spaces -> | some nice text |
print(
    "string without some not needed spaces with left side s.lstrip():",
    "|",
    s.lstrip(),
    "|",
)  # string without some not needed spaces with left side -> | some nice text     |
print(
    "string without some not needed spaces with right sides.rstrip():",
    "|",
    s.rstrip(),
    "|",
)  # string without some not needed spaces with right side -> |    some nice text |
for el in l1:  # element of list without spaces
    l2.append(el.strip())
    """ add into empty list element without spaces from list l1 -> ['John', 'Smith', 'coolmail@mail.com', '+34345456565']"""
    # l2.append(el.lstrip())  # add into empty list element without spaces from list l1 from left side  ['John    ', 'Smith    ', 'coolmail@mail.com    ', '+34345456565    ']
    # l2.append(el.rstrip())  # add into empty list element without spaces from list l1 from right side ['    John', '    Smith', '    coolmail@mail.com', '    +34345456565']
print("list without not needed spaces:", l2)  # result list without not needed spaces
#   print(el.strip(), end=" ")  # deleted spaces and output using one space in one line

s = "    some nice nice text    ".strip()
print("string without spaces:", s)  # some nice nice text
s1 = s.replace("s", "S")  # replace in string "s" into "S"
print(
    'string with replaces letter "s" into "S" s.replace("s", "S"):', s1
)  # "Some nice nice text"
s2 = s.replace(
    "nice", "cool"
)  # replace in string word "nice" into "cool" because two words "nice" in string
print(
    'string with replaces all word "nice" into "cool" s.replace("nice", "cool"):', s2
)  # "some cool cool text", if two "nice" in string, changed all words
s3 = s.replace(
    "nice", "cool", 1
)  # replace in string word "nice" into "cool" because two words "nice" in string
print(
    'string with replaces one word "nice" into "cool" s.replace("nice", "cool", 1):', s3
)  # "some cool nice text", changed only first word and only one word

s4 = s.replace(" nice", "")  # replace in string word "nice" into ""
print(
    'string with replaces one word " nice" into "" s.replace(" nice", ""):', s4
)  # "some text",
s5 = "some nice text"
s6 = "cool nice text"
s7 = "some nice texts"
print(
    'remove prefix "some " from "some nice text" s5.removeprefix("some "):',
    s5.removeprefix("some "),
)  # "nice text"
print(
    'remove prefix "some " from "cool nice text" s6.removeprefix("some "):',
    s6.removeprefix("some "),
)  # "cool nice text"
print(
    'remove prefix "some " from "some nice texts" s7.removeprefix("some "):',
    s7.removeprefix("some "),
)  # "nice texts"

print(
    'remove suffix "text" from "some nice text" s5.removesuffix("text"):',
    s5.removesuffix("text"),
)  # "some nice"
print(
    'remove suffix "text" from "cool nice text" s6.removesuffix("text"):',
    s6.removesuffix("text"),
)  # "cool nice"
print(
    'remove suffix "text" from "some nice texts" s7.removesuffix("text"):',
    s7.removesuffix("text"),
)  # "some nice texts"

l1 = ["1", "2", "n=2", "n=3"]
print("list with out change", l1)
l2 = []
for el in l1:
    l2.append(
        el.removeprefix("n=")
    )  # add element from list l1 to l2 and delete prefix "n="
    # print(el.removeprefix("n="),end=" ") # delete "n="
print("new list without 'n=':", l2)  # ['1', '2', '2', '3']

s5 = "some nice text"
s6 = "cool nice text"
s7 = "some nice texts"

orig = "somenictxl"
trans = "соменіктхл"

trans_tab = str.maketrans(orig, trans)  # create translation table from orig to trans
print(
    'translate string from "some nice text" to "соме ніке техт" s5.translate(trans_tab):',
    s5.translate(trans_tab),
)  # translate string from "some nice text" to "соме ніке техт"
print(
    'translate string from "cool nice text" to "коол ніке техт" s6.translate(trans_tab):',
    s6.translate(trans_tab),
)  # translate string from "cool nice text" to "коол ніке техт"
print(
    'translate string from "some nice texts" to "соме ніке техтс" s7.translate(trans_tab):',
    s7.translate(trans_tab),
)  # translate string from "some nice texts" to "соме ніке техтс"
