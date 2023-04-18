import calendar
import datetime
import time

now = datetime.datetime.now()
print(now)

print(calendar.weekheader(3))

print(calendar.firstweekday())

print(calendar.month(2023,4))

print(calendar.monthcalendar(2023,4))

print("\nloading...")
time.sleep(3)
print("Done!")

print(calendar.calendar(2023))

day_week = calendar.weekday(2023, 4, 13)
print(day_week)

is_leap = calendar.isleap(2023)
print(is_leap)

how_many_leap_days = calendar.leapdays(2020, 2024)
print(how_many_leap_days)

