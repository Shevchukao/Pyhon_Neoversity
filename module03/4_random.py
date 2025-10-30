import random

dice = random.randint(1, 6)  # have start and end, number is Integer
print(f"dice: {dice}")


f1 = random.random()  # float from [0,1)
print(f1)
print(round(10 * f1))  # random number from [0 to 10] no Python way

print(random.randrange(11))  # randrange(11) <-> randint(0,10) [0,11)
print(random.randint(0, 10))  # [0,10]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]  # list with cards
print("all cards list:", cards)  # print all cards
for i in range(10):  # 10 times
    # for _ in range(10):  # _ for stub
    random.shuffle(cards)  # function random shuffle cards in list
print(cards)  # print list with cards

fruits = ["apple", "banana", "orange", "mango"]  # list of fruits
print(random.choice(fruits))  # choise one random fruit from list of fruits

for _ in range(10):  # for loop 0 to 9 (10 times)
    i = random.randint(0, 3)  # random number from 0 to 3, i = [0 ... 3]
    print(fruits[i])  # print one random fruit

for _ in range(10):  # for loop 0 to 9 (10 times)
    print(
        random.choices(fruits, [3, 1, 1, 1], k=3)
    )  # generate list from three elements with weights [3*"apple",1*"banana",1*"orange",1*"mango"]

dictionary_fruits = {"apple": 0, "banana": 0, "orange": 0, "mango": 0}
for _ in range(1000):  # for loop 0 to 9 (10 times)
    chosen = random.choices(fruits, [3, 1, 1, 1], k=3)  # give repeat for choise
    for f in chosen:
        dictionary_fruits[f] += 1
print(dictionary_fruits)

choise = random.sample(
    fruits, k=2
)  # list of k=2 unique random from population sequence first best, second next best
print(choise)

price = random.uniform(50, 100)
print(
    f"price: {price:.2f}"
)  # price float from [50 to 100] with .2f format after dot two number


state = random.getstate()  # get state randomizator
print(random.randint(1, 5))  # number [1-5]
random.setstate(state)  # set state randomizator
print(random.randint(1, 5))  # number [1-5] such as in previosly print
