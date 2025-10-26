debt1 = 0
debt2 = 0
debt3 = 0

while debt1 < 1000:
    print(f"x = {debt1}", end=" ")  # x = range (0 - 990)
    debt1 += 10
print(" ")

while debt2 < 1000:
    debt2 += 10
    print(f"y = {debt2}")  # y = range(10 - 1000)
print(" ")

while debt3 < 1000:
    debt3 += 10
print(f"z = {debt3}")  # z = 1000
print(" ")

# number from 10 to 1
number_desc = 10
while number_desc >= 1:
    print(number_desc)
    number_desc -= 1

# sum odd numbers from 1 to 99
number_asc = 0
total = 0

while number_asc < 100:
    number_asc += 1
    if number_asc % 2 == 0:
        continue
    total += number_asc

number_50_100 = 50
while number_50_100 <= 55:
    if number_50_100 % 7 == 0:
        print(number_50_100)
        break
    number_50_100 += 1
else:
    print("Number not found")

# n = 1
# count = 0

# while n <= 100:
#    if n % 3 == 0 and n % 5 != 0 and sum(int(d) for d in str(n)) > 8:
#        print(n)
#        count += 1
#    n += 1
# print(count)

num = 1
count = 0

while num <= 50:
    if num % 4 == 0 and num % 6 != 0 and sum(int(k) for k in str(num)) % 2 == 0:
        count += 1
    num += 1
print(count)


num_x = 1
count_x = 0

while num_x <= 100:
    if num_x % 7 == 0:
        print("Не нвйдено")
        break
    if num_x % 5 != 0:
        num_x += 1
        continue
    if num_x % 10 == 0:
        num_x += 1
        continue
    if sum(int(k) for k in str(num_x)) <= 10:
        num_x += 1
        continue
    print(num_x)
    num_x += 1


import random


number = random.randint(0, 100)
attempts = 0

try:
    guess = int(input("Guess my number btw 1 and 100 >>> "))
    guess = guess / 0
except ValueError:
    guess = int(input("ValueError. Please enter integer number between 1 to 100: "))
    while attempts < 10:
        attempts += 1
        if guess > number:
            print(f"{guess} is too high")
        elif guess < number:
            print(f"{guess} is too low")
        else:
            print(f"Congrats, you won in {attempts} attempts")
            break

        guess = int(input("Guess again please: "))
    print(f"You win")
except ZeroDivisionError:
    guess = int(
        input("ZeroDivisionError. Please enter integer number between 1 to 100: ")
    )
    while attempts < 10:
        attempts += 1
        if guess > number:
            print(f"{guess} is too high")
        elif guess < number:
            print(f"{guess} is too low")
        else:
            print(f"Congrats, you won in {attempts} attempts")
            break

        guess = int(input("Guess again please: "))
    print(f"You win")
except:
    guess = int(input("Error. Please enter integer number between 1 to 100: "))
    while attempts < 10:
        attempts += 1
        if guess > number:
            print(f"{guess} is too high")
        elif guess < number:
            print(f"{guess} is too low")
        else:
            print(f"Congrats, you won in {attempts} attempts")
            break

        guess = int(input("Guess again please: "))
    print(f"You win")
else:
    while attempts < 10:
        attempts += 1
        if guess > number:
            print(f"{guess} is too high")
        elif guess < number:
            print(f"{guess} is too low")
        else:
            print(f"Congrats, you won in {attempts} attempts")
            break

        guess = int(input("Guess again please: "))
    print(f"You win")
finally:
    print("Goodbye")


try:
    save_user_in_db()
except:
    rollack()
    print("File does not existds")
else:
    save()
finally:
    print("Goodbye")
