def main():
    numbers = [-3, -2, -1, 0, 0.5, 1, 1.5, 2, 2.5, 3]

    for x in numbers:
        print(f(x))


def f(x):
    return((3*x-2)**2)


if __name__ == "__main__":
    main()
