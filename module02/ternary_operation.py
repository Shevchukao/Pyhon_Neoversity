number = int(input("Enter a number: "))

if number >= 0:
    print(f"Not a negative number: {number}")
else:
    print(f"Negative number: {number}")

(
    print(f"Not a negative number: {number}")
    if number >= 0
    else print(f"Negative number: {number}")
)


some_data = input("Enter some words or numbers: ")
msg = some_data or "No data"
print(msg)
