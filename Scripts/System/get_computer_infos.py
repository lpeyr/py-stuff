import platform


def main():
    p = platform.uname()

    print(
        f"\nYour processor is:\n{p.processor}\n\nArchitecture:\n{p.machine}\n\nSystem:\n{p.system}\n\nName:\n{p.node}")


if __name__ == "__main__":
    main()
