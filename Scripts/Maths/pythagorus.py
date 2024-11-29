def square_sum(a, b):
    return a * a + b * b


def main():
    a = int(input("Enter the first side the triangle: "))
    b = int(input("Enter the second side the triangle: "))
    c = int(input("Enter the third side the triangle: "))

    if (square_sum(a, b) % c == 0):
        print("The triangle is right.")
    else:
        print("The triangle isn't right.")


if __name__ == "__main__":
    main()
