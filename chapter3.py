price = 0.51
month = 30
day = 24
money = 918

perday = price * day
perday20 = perday * 20
permonth = perday * month
permonth20 = permonth * 20


daysoperate = money / perday


print('total per day is: ${:.2f}.'.format(perday))
print('total per month is: ${:.2f}.'.format(permonth))

print('total per day for 20 servers is: ${:.2f}.'.format(perday20))
print('total per month for 20 servers is: ${:.2f}.'.format(permonth20))
print('number of days to operate: ' + format(daysoperate)) 
