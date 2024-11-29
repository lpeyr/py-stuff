# Get the number of days in a specific month

from calendar import monthrange

year = 2021
month = 9

num_days = monthrange(year, month)[1]  # 30
