import re

date_regex = re.compile(r'(\d{1,2})\/(\d{1,2})\/(\d{4})')

text_date = "In the 29/02/1601 something happened. As well as in the 12/01/1999. Every day something happens. But not in 29/02/1600..."


def check_general_values(day, month, year):
    # Check values for day, month and year
    if not (0 < day <= 31) or not(0 < month <= 12) or not(1000 < year <= 2999):
        print("Not valid values")
        return False

    # Check day related to month
    if (month == 2 and day > 29) or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
        print("Not valid days")
        return False

    # Check if year is leap
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Year is leap, february day can't be > 28")
        return False

    print(f"{day:02d}/{month:02d}/{year} is a valid date")


# results is a list of tuples
results = date_regex.findall(text_date)

for group in results:
    # Each group is a tuple of 3 strings ('dd', 'mm', 'yyyy')
    day, month, year = group
    check_general_values(int(day), int(month), int(year))
