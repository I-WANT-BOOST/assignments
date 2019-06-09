hours=(45)
rate=(10)
if hours>40:
    pay=((hours-40)*(rate)*(1.5))+((40)*(rate))
else:
    pay=(hours)*(rate)
print(pay)
