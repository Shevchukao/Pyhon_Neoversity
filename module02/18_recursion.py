def fact(n):
    if n == 1:  # if statement for stop recursion
        return 1
    return n * fact(n - 1)


n = 5  # number of factorial
print(f"factorial {n}:", fact(n))
# n! = n*(n-1)*(n-2)*...*2*1
