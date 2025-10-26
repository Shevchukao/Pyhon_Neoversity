fruit = "watermelon"

match fruit:
    case "apple":
        print("It's an apple")
    case "pear":
        print("It's a pear")
    case "watermelon":
        print("It's a watermelon")
    case _:
        print("It's an unknown fruit")

fruit = ["mouse", "cat", "dog"]

match fruit:
    case ["cat", "dog", _]:
        print("They're cat and dog")
    case ["dog", _, _]:
        print("It's a dog")
    case ["cat", _, _]:
        print("It's a cat")
    case _:
        print("They're unknown animals")

point = (394, 253, 344)

match point:
    case (0, 0):
        print("It's a point at the center of coordinates")
    case (x, 0):
        print(f"It's a point on the x axis ({x}, 0)")
    case (0, y):
        print(f"It's a point on the y axis (0, {y})")
    case (x, y):
        print(f"It's a point with coordinate ({x}, {y})")
    case _:
        print(f"It isn't a point")
