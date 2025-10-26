print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer_1 = int(input("Enter tour answer (1-2): "))
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer_2 = int(input("Enter your answer (1-4): "))
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer_3 = int(input("Enter your answer (1-4): "))

a = 0
if answer_1 == 1:
    gryffindor = a + 1
    ravenclaw = a + 1
    hufflepuff = a
    slytherin = a
elif answer_1 == 2:
    hufflepuff = a + 1 
    slytherin = a + 1
    gryffindor = a
    ravenclaw = a
else:
    print("Wrong input.")

if answer_2 == 1:
    hufflepuff = hufflepuff + 2
elif answer_2 == 2:
    slytherin = slytherin + 2
elif answer_2 == 3:
    ravenclaw = ravenclaw + 2
elif answer_2 == 4:
    gryffindor = gryffindor + 2
else:
    print("Wrong input.")

if answer_3 == 1:
    slytherin = slytherin + 4
elif answer_3 == 2:
    hufflepuff = hufflepuff + 4
elif answer_3 == 3:
    ravenclaw = ravenclaw + 4
elif answer_3 == 4:
    gryffindor = gryffindor + 4
else:
    print("Wrong input.")

print("gryffindor:", gryffindor, "hufflepuff:", hufflepuff, "ravenclaw:", ravenclaw, "slytherin:", slytherin)