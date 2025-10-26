def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        x = " " * ((length - len(string)) // 2)
        print(x)
        return x + string


print(format_string("Anton Shevchuk", 24))
