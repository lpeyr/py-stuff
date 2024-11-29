def selector():
    c = int(input("Which mode do you want to choose?\n\n1. See divisors of a number.\n2. See common divisors of two numbers.\n"))
    if c > 2 or c == 0:
        print("\nIncorrect choice.\n")
        selector()
    elif c == 1:
        get_divisors()
    elif c == 2:
        get_common_divisors()
    selector()


def get_common_divisors():
    k = int(input("Enter the first number: "))  # Demander les nombres
    n = int(input("Enter the second number: "))  # Demander les nombres

    print("\n")  # New line

    if k == 0 or n == 0:
        print("Please choose another number than zero.")
        get_common_divisors()

    dk = []  # Divisor number 1
    dn = []  # Divisor number 2
    divisor = []  # Common divisors

    # Number 1
    for i in range(k + 1):
        if i > 0:
            if k % i == 0:
                dk.append(k / i)

    # Number 2
    for i in range(n + 1):
        if i > 0:
            if n % i == 0:
                dn.append(n / i)

    # Show results
    for i in range(len(dk)):
        if dn.__contains__(dk[i]):
            divisor.append(dk[i])

    if len(divisor) != 0:
        for i in range(len(divisor)):
            print(
                f"{divisor[i]} is divisor of {k} and of {n}")
    else:
        print("These two numbers don't have any divisors in common.")

    print("\n")  # New line


def get_divisors():
    n = int(input("Enter a number: "))
    print("\n")  # New line

    for i in range(n + 1):
        if i > 0:
            if n % i == 0:
                print(f"{n} is divisible by {i}")
    print("\n")  # New line


def main():
    selector()  # Start program selector


if __name__ == "__main__":
    main()
