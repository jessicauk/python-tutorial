import datetime

# print(help(datetime.date))

gvr = datetime.date(1956, 1, 31)
print(gvr)
# day
print(gvr.day)
# month
print(gvr.month)
# year
print(gvr.year)

mill = datetime.date(2000, 1, 1)
print(mill)
dt = datetime.timedelta(100)
print(mill + dt)

# dateformat
# Day-name, Month-name Day-#, Year
print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d,%Y}."
print(message.format(gvr))