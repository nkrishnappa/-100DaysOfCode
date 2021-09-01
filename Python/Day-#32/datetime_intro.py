import datetime

now = datetime.datetime.now()
print(now.day) # 1
print(now.weekday()) # 2
print(type(now)) # <class 'datetime.datetime'>
print(now.year) # 2021
print(now) # 2021-09-01 08:48:28.073896

date_of_birth = datetime.datetime(year=1993, day=15, month=6)
print(date_of_birth) # 1993-06-15 00:00:00