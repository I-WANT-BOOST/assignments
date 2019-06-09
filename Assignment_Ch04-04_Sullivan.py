timeOfCall = input('Enter the time the call starts in 24-hour notation:\n')
hour = int(timeOfCall[0:2])
minute = int(timeOfCall[3:5])/60
print(hour+minute)

day = input('\nEnter the first two letters of the day of the week:\n')

length = input('\nEnter the length of the call in minutes:\n')
callLength = float(length)


def calculateTotalCost(hour,minute,day,callLength):
    print(hour+minute)
    if 8.00<=(hour+minute)<=18.00 and (day.upper()=='MO' or day.upper()=='TU' or day.upper()=='WE' or day.upper()=='TH' or day.upper()=='FR'):
        cost = callLength * 0.40
    elif ((hour+minute)>18.00 or (hour+minute)<8.00) and (day.upper()=='MO' or day.upper()=='TU' or day.upper()=='WE' or day.upper()=='TH' or day.upper()=='FR'):
        cost = callLength * 0.25
    elif day.upper()=='SA' or day.upper()=='SU':
        cost = callLength * 0.15
    return cost

cost = calculateTotalCost(hour,minute,day,callLength)

print('Cost of the call: $','{:.2f}'.format(cost))
