value = 7
match value:  # match statement(subject whose value is testing) # match-case: for pattern matching, alternative to complex if-elif-else
    case (
        5
    ):  # case block contain patterns and Python compares the subject in each case from top to bottom
        print("five")
    case 7:  # the code block for the first pattern that matches is executed
        print("seven")
    case 10:
        print("ten")
    case (
        _
    ):  # case _; pattern act as a default or catch-all block, executing if no other patterns match
        print("another value")


value3 = 5
value4 = 5
match value3, value4:
    case 5, 5:
        print("five")
    case 7, value4:
        print("seven")
    case value3, 10:
        print("ten")
    case _:
        print("another value")

value1 = "del"
value2 = "C:\delme"
match value1, value2:
    case value1, "C:\windows":
        print("C:\windows is untouchable")
    case "del", value2:
        print(f"remove {value2}")
    case _:
        print("another value")
