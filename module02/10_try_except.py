# f = None
# try:
#     10 / 0  # 10 devide by 0, ZeroDivisionError
#     f = open("c:\\absent.txt", "rb")  # open file which we don't have, FileNotFoundError
# # except ZeroDivisionError as e:  # work only with Error type ZeroDivisionError
# except Exception as e:  # work with many exceptions
#     print(type(e))  # class 'ZeroDivisionError or <class 'FileNotFoundError'>
#     print(
#         f"Error: {e}"
#     )  # print Error: and (division by zero/ [Errno 2] No such file or directory: 'c:\\absent.txt')
# print("Done")  # print alweys when we have Exception


# f = None
# try:
#     # 10 / 0
#     # f = open("c:\\absent.txt", "rb")
#     raise TabError  # raise(вызвать вручную)
# except Exception as e:  # Error as e == (TypeError assignment to variable e)
#     if isinstance(e, ZeroDivisionError):
#         print("division by 0")  # comand "pass" -> Skip the step/action
#     elif isinstance(e, FileNotFoundError):
#         print("no file")
#     else:
#         print(f"Error: {e}")
# print("Done")  # print alweys when we have

f = None
try:
    # 10 / 0
    f = open("c:\\absent.txt", "rb")
    # raise TabError  # raise(вызвать вручную)
except Exception as e:
    if isinstance(e, ZeroDivisionError):  # if ZeroDivisionError => print
        print("division by 0")  # comand "pass" -> Skip the step/action
    else:  # else Error, if not ZeroDivisionError
        print(f"Error: {e}")  # print Error no stop loops
        raise e  # Error, stop loops
finally:  # always do after loops
    if f is not None:
        f.close()

print("Done")  # print alweys when we have Exception
