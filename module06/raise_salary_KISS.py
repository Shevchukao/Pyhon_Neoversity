def raise_salary(old_salary, raise_value):
    brutto_salary = old_salary + raise_value
    netto_salary = brutto_salary * 0.9 if brutto_salary <= 1000 else brutto_salary * 0.8

    return {"brutto": brutto_salary, "netto": netto_salary}


# VERY HARD
def is_even(n: int) -> bool:
    if n % 2 == 1:
        return True
    else:
        return False


# HARD
def is_even(n: int) -> bool:
    if n % 2 == 1:
        return True
    return False


# EASY
def is_even(n: int) -> bool:
    return n % 2 == 1


if __name__ == "raise_salary":
    print("you are using cool module 'A'")
if __name__ == "__main__":
    print(raise_salary(1000, 0))
    print(raise_salary(1000, 100))
