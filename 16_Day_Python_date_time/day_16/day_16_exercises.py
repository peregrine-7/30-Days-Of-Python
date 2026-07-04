from datetime import datetime, date, timedelta

print(dir(datetime))

now = datetime.now()

print(now)

timestamp = now.timestamp()
print(timestamp)



d = date(2020, 1, 1)
print(d)
print(d.today())

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time:", t)
time_string = '5 December, 2019'
date_object = datetime.strptime(time_string, "%d %B, %Y")
print(date_object)

today = date(year=2026, month=7, day=4)
new_year = date(year=2027, month=1, day=1)
time_left = new_year - today
print(time_left)
start_year = date(year=1970, month=1, day=1)
from_start = today - start_year
print(from_start)


