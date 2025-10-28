# while True:  # infinite loop in games, server application, gui; for programs that need to run forever as background services (daemons); (robust code that retries an action, like a network connection, until it succeeds)

# Example:
# while True:
#     user_input = input("Enter 'yes' or 'no': ").lower()
#     if user_input in ("yes", "no"):
#         print(f"You entered: {user_input}")
#         break  # Exit the loop
#     else:
#         print("Invalid input, please try again.")


# a = 1
# while True:  # infinite loop, for stop loop using CTRL+C
#     a += 1
#     print(a)

# a = 1
# while True:  # Not infinite loop because we have break and if statement
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)
#     if a > 1000:
#         break

# a = 1
# while True:  # Not infinite loop because we have break and if statement
#     cmd = input("Enter a comand: ")
#     match cmd:
#         case "add":  # add  a = a + 1
#             a += 1
#         case "sub":  # substraction  a = a - 1
#             a -= 1
#         case "print":  # print a
#             print(a)
#         case "print *":
#             print("*" * a)  # print "*" a times
#         case "exit":
#             break  # exit from loop
#         case _:
#             print("unknown command")  # when enter not correct command


while True:
    inp = input(
        "Enter a comand cd/mkdir/rm/exit: "
    )  # enter a comand format cd/md/rm or exit for end loops
    inp = (
        inp.split()
    )  # creating lists from entering comand (split text with spaces sep = " ")
    print("list from entering comand: ", inp)
    cmd = inp[0]  # comand for check match-case
    print("first element of list for match-case: ", cmd)
    inp = inp[1:]  # directory or directories in list
    print("slice for directory or directories: ", inp)
    match cmd:  # check variable cmd(first element list)
        case "mkdir":  # compare command with pattern mkdir
            print(
                f"Make directories: {inp}"
            )  # print directory or directories what we make
        case "cd":
            print(
                f"Changing directories: {inp[0]}"
            )  # print only first element from slice inp = inp[1:], second ad other deleted
        case "rm":
            print(
                f"Removing directories: {inp}"
            )  # print directory or directories what we deleted
        case "exit":
            break  # exit from loop
        case _:
            print("unknown command")  # when enter not correct command
