print(range(5))  # range(0, 5)

for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

def sq_gen(n=10):
    i = 0
    while i < n:
        i +=1
        yield i * i


if __name__ == "__main__":
    for i in sq_gen():
        print(i, end=" ")  # 1 4 9 16 25 36 49 64 81 100
