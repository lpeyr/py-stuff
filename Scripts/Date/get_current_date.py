import datetime


def main():
    current_date = datetime.datetime.now()

    year = current_date.year
    month = current_date.month
    day = current_date.day

    print(f"{day}/{month}/{year}")


if __name__ == "__main__":
    main()
