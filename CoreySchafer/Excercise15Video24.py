import datetime

"""
d = datetime.date(2024, 4, 12)
print(d)

tdy = datetime.date.today()
print(tdy.weekday())
print(tdy.isoweekday())

#tdelta 
tdelta = datetime.timedelta(days=7)
print(tdy+tdelta)
print(tdy - tdelta)

bday = datetime.date(2024,9,9)
tday = (bday - tdy)
print(tday.total_seconds())



ti = datetime.time()
print(ti)
tdate = datetime.datetime(2016, 4, 12, 12 ,30)
print(tdate)
print(tdate.time())

tdate = datetime.datetime(2016, 4, 12, 12 ,30)
print(tdate)
print(tdate.year)
print(tdate.day)
print(tdate.month)

tdel = datetime.timedelta(days = 7 )
print(tdate + tdel)
"""
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.now(datetime.timezone.utc)

print(f"today:{dt_today}\n, now:{dt_now}\n, utc:{dt_utcnow}")


