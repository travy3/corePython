from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2016,6,16,10,15)
print(dt)

#timestamp 相对于epoch time（19700101）的秒数

print(dt.timestamp())

#str--> datetime
cday = datetime.strptime('2015-6-1 18:10:23', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime --> str

print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#datetime +-
print(now+timedelta(hours=10))

