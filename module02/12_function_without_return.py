def findLetter(st: str, letter: str) -> str | None:
    counter = 0  # counter
    for let in st.lower():  # loop let = [letter from sting st] other for each iteration
        if (
            let == letter
        ):  # compare let = [letter from sting st] with letter in function
            return counter  # return number iteration/step/loop
        counter += 1  # counter = counter + 1 for other iteration
    return None


st = "Anton Shevchuk"
print("String: ", st)
letter = "a"
print("Letter: ", letter)
print(findLetter(st, letter))
letter = "o"
print("Letter: ", letter)
print(findLetter(st, letter))
letter = "s"
print("Letter: ", letter)
print(findLetter(st, letter))

# if findLetter(st, "a"):  # don't use because, return var counter = 0 in bool False -> not found
#     print("found")
# else:
#     print("not found")

if findLetter(st, "a") is not None:  # 0 is not None -> True -> found
    print("Letter a is found")
else:
    print("Letter a is not found")
