year = int(input("Year: "))
if year % 4 == 0 and (year % 100 != 0 and year % 400 == 0):
    next_leap_year = year + 4
else:
    next_leap_year = year + (4 - year % 4)
    if next_leap_year % 100 == 0 and next_leap_year % 400 != 0:
        next_leap_year += 4
print(f"The next leap year after {year} is {next_leap_year}")

