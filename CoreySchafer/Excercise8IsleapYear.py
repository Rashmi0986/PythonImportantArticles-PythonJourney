def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31,30 ,31 ,30 ,31]

def days_in_month(year, month):
    if not 1 <= month <=12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

year = 2020
month = 3
print(is_leap(year))
print(days_in_month(year, month))

