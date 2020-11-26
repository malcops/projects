import datetime

day = datetime.date(1901, 1, 1)

count = 0
while day.year != 2001:
    if (day.day == 1) and (day.weekday() == 6):
        count += 1
    day += datetime.timedelta(days=1)

print("answer: {}".format(count))

