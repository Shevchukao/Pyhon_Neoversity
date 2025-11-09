# print(range(5))  # range(0, 5)

# for i in range(5):
#     print(i, end=" ")  # 0 1 2 3 4
# print()


# def sq_gen(n=10):
#     i = 0
#     while i < n:
#         i += 1
#         yield i * i  # return one values, yield many values


def reader(filename: str):
    l = " "
    with open(filename, "r") as f:
        while l != "":
            l = f.readline().strip()
            yield l.split()


with open("text.txt", "w") as f:
    f.write(
        """ Some long and funny
            Text is here
            To show us
            How to use
            and why to use
            generators.
    """
    )
if __name__ == "__main__":
    #     # for k in sq_gen():
    #     #     print(k, end=" ")  # 1 4 9 16 25 36 49 64 81 100
    #     list_1 = [i for i in sq_gen()]  # comprehensions
    #     print(list_1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for line in reader("text.txt"):
        if line[0] == "To":
            break
        # ['Some', 'long', 'and', 'funny']
        # ['Text', 'is', 'here']
        print(line)
