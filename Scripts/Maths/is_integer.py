def is_interger(x: float):
    return int(x) == x


def main():
    x = float(input("Enter a number. "))
    if is_interger(x):
        print("The number is an integer.")
    else:
        print("The number isn't an integer.")


if __name__ == "__main__":
    main()
