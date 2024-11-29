import datetime
from calendar import monthrange


def main():

    total_data = float(
        input("What is the total amount of data do you have? (in GB) "))

    reset_day = int(
        input("What day of the month is your data consumption reset? "))

    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    last_month = datetime.datetime.now().month - 1

    start_date = datetime.datetime(current_year, last_month, reset_day)
    end_date = datetime.datetime(current_year, current_month, reset_day)

    num_days = (end_date - start_date).days
    num_days_elapsed = (datetime.datetime.now() - start_date).days
    data_consumed = total_data / num_days * num_days_elapsed

    # Check if the number is an int
    data_consumed = round(data_consumed, 2)
    if data_consumed.is_integer():
        data_consumed = int(data_consumed)

    print(
        f"Today, you should've consumed {data_consumed} GB\n{num_days_elapsed} days have passed since your data consumption reset")


if __name__ == "__main__":
    main()
