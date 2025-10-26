username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "querty":
        print("Login successfull! Welcome admin!")
    elif password == "123456":
        print("Weak password! Change it immediately")
    else:
        print("Incorrect password")
elif username == "guest":
    if password == "guest_sun":
        print("Login successfull! Welcome guest!")
    else:
        print("Incorrect password")
else:
    print("Go to school!")


age = 19

if age >= 18 and type(age) == int and age <= 50:
    print(f"Your age is normal! {type(age)}")
    print("Your age is normal! {}".format(type(age)))
