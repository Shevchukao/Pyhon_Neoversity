import time

s1 = "Hello world"  # string with quotes
s2 = "Hello world"  # string with double quotes
text1 = """ Hello world 
and Python """  # string with many rows
text2 = (
    "very long text is here to " "show how it works"
)  # string with one row for Python
# long string divide on many rows use "str " \ "str" , don't use some symbols after \ (work as concatenation)
text3 = "very long text is here to\nshow how it works"  # /n - new line
text4 = "very long text is here to\tshow how it works"  # /t - tab character between to and show
text5 = "1\t2\t45\t100\n100\t45\t2\t1"  # for column output using 8 symbols between tab element
text6 = "12345678\t2\t45\t100\n100\t45\t2\t1"  # output using 8 symbols tab shift right on 8 symbols
text7 = "text pt 1\vtext pt 2"  # see variable text8, in Linux it's output such as text8
text8 = """text pt 1               
                    text pt 2"""  # "text pt 1\n\t text pt 2" \n\t == \v(Linux)
text9 = "text pt 1\b\b\btext pt 2"  # string where backspace escape sequence (\b) is used to move the cursor backward

for i in range(101):  # for loop generation number from 0 to 100
    print(
        f"{i}% Ready", end="\r"
    )  # print output on the same line use \r carriage return cursor to beginning of the current line without advancing to the next one.
    time.sleep(0.01)  # pauses scripts execution
print("Done" + " " * 10)  # final print after loop

print(
    s1, s2, text1, text2, text3, text4, text5, text6, text7, text9, sep="\n"
)  # sep separator = "\n" - new line, output all of text will be from new row
""" Output 
Hello world
Hello world
 Hello world
and Python
very long text is here to show how it works
very long text is here to
show how it works
very long text is here to       show how it works
1       2       45      100
100     45      2       1
12345678        2       45      100
100     45      2       1
"""

print(
    ' "\\ \077'
)  # escape character \ (\": Interpreted as a literal double quote (").) (\\: Interpreted as a literal backslash (\).)
# \077: this is an octal escape sequence, 077: interpreted as an octal (base-8) number, the octal value 077 converts to the decimal value 63, The ASCII character with the decimal value 63 is the question mark (?).
