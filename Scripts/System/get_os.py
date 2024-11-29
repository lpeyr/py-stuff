import platform


def main():
    os = platform.uname()

    print(
        f"You are using {os.system}, version {os.release} ({os.version}).")


if __name__ == "__main__":
    main()
