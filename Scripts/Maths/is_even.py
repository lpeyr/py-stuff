def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    even = is_even(int(input("Enter a number : ")))
    if even == True:
        print("The number is even")
    else:
        print("The number isn't even")


if __name__ == "__main__":
    main()
