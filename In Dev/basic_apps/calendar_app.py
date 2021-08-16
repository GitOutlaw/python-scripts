import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021, 8))

print(calendar.monthcalendar(2020, 8))

print(calendar.calendar(2021))

day_of_the_week = calendar.weekday(2021, 8, 25)

is_leap_year = calendar.isleap(2021)

print(is_leap_year)

# outputs how many leap years range
how_many_leap_days = calendar.leapdays(2000, 2021)

print(how_many_leap_days)