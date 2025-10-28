a = 5
print("a:", a)
# loop while
while a > 0:  # while condition: if True -> body, if False -> exit from loop
    print("a from 5 to 1, because print before a -= 1: ", a)  # | body loop start
    a -= 1  ### | body loop finish -> go to check while condition

b = 5
print("b:", b)
while b > 0:  # while condition: if True -> body, if False -> exit from loop
    b -= 1  # b = b - 1 on each loop
    print("b from 4 to 0, because print after b -= 1: ", b)  # check while condition
