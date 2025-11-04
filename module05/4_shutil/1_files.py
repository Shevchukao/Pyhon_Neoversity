# f1 = open("test.txt", "w")   # Don't work with this method
# f1.write("some\nfunny\ntext")
# f1.close()

# def fun1():  # difference fun1 and fun1()
#     return 3
# f = fun1  # link
# print(fun1)  # <function fun1 at 0x00000299960D1760>
# print(fun1())  # 3
# print(f())  # 3


# with open(
#     "test.txt", "w"
# ) as f1:  # Python not need close file if we use with ... as ...: (with - it's context manager)
#     f1.write("some\n  funny\n  text")  # # write
# # with open("test.txt", "r") as f2:  # read
# with open("1_files.py", "r") as f2:  # read
# text = f2.read()  # read charecters from stream [some funny text] -> vertical
# text = (
#     f2.readlines()
# )  # create list from stream ['some\n', 'funny\n', 'text'] with \n
# text = [line.strip() for line in text]  # ['some', 'funny', 'text'] delete all whitespaces
# text = [
#     line.rstrip() for line in text
# ]  # ['some', 'funny', 'text'] delete whitespaces from right
# print(text)
# for line in text:
#     print(line)

# Python Way text = f2.readlines(); text = [line.rstrip() for line in text]
# text = [line.rstrip() for line in f2.readlines()]
# for line in text:
#     print(line)

# w - Write      | Create file or recreate file
# w+             | Delete file, create file and change position cursor in end of file(append)
# r - Read       | For reading file
# r+             | Not create not delete and change cursor position in start of file
# a - Append     | Adding new data in the end of file
# a+             | Create not delete and change cursor position in end of file
# b - Binary     | Binary mode
# t - Text       | Text mode (using by default with other)
# + - Additional | Open for  read and write (ADD)
# x - exclusive  | Create file and open for write, if file created early - Exception!!!


# with open("test.txt", "w+") as f1:
#     f1.write("some another\nfunny an joyfull\nvery big text")  # write from 1 to 3 row
#     print(f1.tell())  # return current stream position of write cursor(45)
#     print(
#         f1.read()
#     )  # read after text on 3 row in end and also no output only whitespaces(need change position cursor)
#     f1.seek(0)  # change position cursor on 0 position
#     print(f1.read())  # read from 0 position
#     print(
#         f1.tell()
#     )  # return current stream position of read cursor(45 symbols include /n as two position)
#     f1.seek(5)
#     f1.write("other")  # change another to otherer
#     f1.seek(45)
#     f1.seek(f1.tell() - 4)  # f1.tell() return 45 and  - 4 = 41
#     f1.write("book")  # change text to book

# with open("test.txt", "r+") as f1:
#     f1.write("some anoth\n funny an joyfull\nvery big text")
#     f1.seek(0)
#     buf = " "  # or None
#     while buf != "":  # while not eof(f1)
#         # buf = f1.read(5)  # read 5 symbols in line
#         # buf = f1.readline()  # read by one row in line
#         # buf = f1.readline().rstrip()  # read by one row in line without right whitespaces
#         buf = f1.readline().strip()  # read by one row in line without all whitespaces
#         print(f"|{buf}|")


# def process(x):
#     pass


# with open("test.txt", "r+") as f1:
#     f1.write("some anoth\n funny an joyfull\nvery big text")
#     f1.seek(0)
# ***NOT GOOD*** (using only if file is small)
# text = f1.read()
# lines = text.split("\n")
# # words = [line.split(" ") for line in lines] # with whitespaces
# words = [line.strip().split(" ") for line in lines]  # without whitespaces
# process(words)
# print(words)


# ***GOOD***
def process(x):
    pass


with open("test.txt", "r+") as f1:
    f1.write("some anoth\n funny an joyfull\nvery big text")
    f1.seek(0)
    buf = " "  # or buf = None
    words = []  # empty list
    while buf != "":  # while not eof(f1)
        buf = f1.readline()  # read one line
        buf_l = (
            buf.rstrip().split()
        )  # delete whitespaces and create list element of string
        process(buf_l)  # call function
        words.append(buf_l)  # append empty list lists buf_l
    print(
        words
    )  # [['some', 'anoth'], ['funny', 'an', 'joyfull'], ['very', 'big', 'text'], []]
