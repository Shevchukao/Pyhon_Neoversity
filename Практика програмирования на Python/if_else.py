print("What is your name? ")
name = input()
print("Hello ", name, "!", sep="")
age = int(input("How old are you, " + name + "? "))
print("I think you are", age + 1, end=" ")
age_1 = age + 1
if age_1 == 1:
    print("year.")
else:
    print("years.")
