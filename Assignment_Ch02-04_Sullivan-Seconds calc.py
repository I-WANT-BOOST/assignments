total_seconds = int(input('Enter the elapsed time in seconds:'))


print('The elapsed time in seconds =',total_seconds)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = (total_seconds % 3600) %60

print('The equivalent time in hours:hours:minutes:seconds =',hours,':',minutes,':',seconds)
