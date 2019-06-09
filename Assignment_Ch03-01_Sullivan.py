num1,num2,num3=input('please enter three numbers:').split()

num1=int(num1)
num2=int(num2)
num3=int(num3)

if num1<=num2<=num3:
  print('The three integer numbers in ascending order:''\n',num1,num2,num3)
elif num1<=num3<=num2:
  print('The three integer numbers in ascending order:''\n',num1,num3,num2)
elif num2<=num1<=num3:
  print('The three integer numbers in ascending order:''\n',num2<=num1<=num3)
elif num2<=num3<=num1:
  print('The three integer numbers in ascending order:''\n',num2,num3,num1)
elif num3<=num2<=num1:
  print('The three integer numbers in ascending order:''\n',num3,num2,num1)
elif num3<=num1<=num2:
  print('The three integer numbers in ascending order:''\n',num3,num1,num2)
