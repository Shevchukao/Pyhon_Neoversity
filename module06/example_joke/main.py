from joke import get_random_joke

print(dir())


def main():
    name = input("Input your name: ")
    print(f"Hello, {name}!")

    while True:
        user_response = input(f"{name}, could you listen joke? (yes/no) ").lower()
        print(user_response)
        if user_response == "yes":
            print(get_random_joke())
        if user_response == "no":
            print(f"Good bye, {name}")
            break


if __name__ == "__main__":
    main()
