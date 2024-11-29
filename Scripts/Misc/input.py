# Basic input

def main():
    name = input("What's your name?\n> ")
    age = input("How old are you?\n> ")
    print("Hello, {name}!".format(name=name))


if __name__ == "__main__":
    main()
