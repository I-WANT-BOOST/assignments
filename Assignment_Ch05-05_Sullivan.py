def validateUserInput():
    while True:

        firstNum, secondNum = input('\nEnter two positive integer numbers.\nThe first must be less than the second.\nnumbers:').split()

        try:  #First we check that the inputs are integers. anything other than an integer will error.
            firstNum = int(firstNum)
            secondNum = int(secondNum)
        except: #if not, we notify the user and loop.
            print('\nIncorrect Input. \nPlease try again.\n\n')
            continue

        if firstNum < 0 or secondNum < 0: #next we check if the inputs are less then zero (negative).
            print('\nNo negative Numbers!\nPlease try again.\n\n')
            continue

        if firstNum > secondNum: #finally, we check if the first number is smaller than the second.
            print('\nThe first number must be less than the second number!\nPlease try again.\n\n')

        else: #if all requirements for input are met, we break the loop.
            break

    return (firstNum, secondNum)








def oddNumbers(firstNum,secondNum):
    numList = []  #variables need to be established before the loop, to avoid over writing the lists.

    oddList = []

    count = firstNum - 1 #this needs to be done before the loop so that the first number is included. (count starts at 0)

    while True:

        count = count + 1

        numList.append(count)

        if count == secondNum :
            break                       #once we loop to the second number, we break the loop.

        else:
            for i in numList: # % 2 to check if the number is odd.
                if i % 2 != 0:
                    odd = i
                else: # if we don't assign zero to odd, the next loop will just skip the if block and add the last assigned number.
                    odd = 0

        oddList.append(odd) #add odd to oddList

        if 0 in oddList: #check for and remove any zeros from the for loop.
            oddList.remove(0)

    if secondNum % 2 != 0:
        oddList.append(secondNum)

    print('\nOdd integers between',firstNum,'and',secondNum,'are:\n',*oddList, sep=' ')







def sumEvenNumbers(firstNum,secondNum):
    numList = []  #variables need to be established before the loop, to avoid orwriting the lists.

    evenList = []

    count = firstNum - 1 #this needs to be done before the loop so that the first number is included. (count starts at 0)

    while True:

        count = count + 1

        numList.append(count)

        if count == secondNum:
            break                       #once we loop to the second number, we break the loop.

        else:
            for i in numList: #same as B Loop but for even numbers.
                if i % 2 == 0:
                    even = i
                else:
                    even = 0
            evenList.append(even)

    if secondNum % 2 == 0:
        evenList.append(secondNum)

    return sum(evenList)






def sumSquareOddNumbers(firstNum,secondNum):
    oddSquareList = []

    numList = []  #variables need to be established before the loop, to avoid orwriting the lists.

    oddList = []

    count = firstNum - 1 #this needs to be done before the loop so that the first number is included. (count starts at 0)

    while True:

        count = count + 1

        numList.append(count)

        if count == secondNum :
            break                       #once we loop to the second number, we break the loop.

        else:
            for i in numList: # % 2 to check if the number is odd.
                if i % 2 != 0:
                    odd = i
                else: # if we don't assign zero to odd, the next loop will just skip the if block and add the last assigned number.
                    odd = 0

            oddList.append(odd) #add odd to oddList

        if 0 in oddList: #check for and remove any zeros from the for loop.
            oddList.remove(0)

    if secondNum % 2 != 0:
                oddList.append(secondNum)

    count = firstNum -1

    while True:

        count = count + 1

        numList.append(count)

        if count == secondNum :
            break                       #once we loop to the second number, we break the loop.

        for i in oddList: #calculates the square of each odd number and puts it in a new list.
            square = i ** 2
            oddSquareList.append(square)

        if len(oddSquareList) == len(oddList):
            break

    return sum(oddSquareList)





def main():
    while True:

        firstNum, secondNum = validateUserInput()

        oddNumbers(firstNum,secondNum)

        sumEven = sumEvenNumbers(firstNum,secondNum)

        print('\nSum of even integers between',firstNum,'and',secondNum,'=',sumEven)

        sumSquareOdd = sumSquareOddNumbers(firstNum,secondNum)

        print('\nSum of the squares of odd integers between',firstNum,'and',secondNum,'=',sumSquareOdd)




        while True:
            check = input("\n\nwould you like to repeat this program? \n(y/n)\n>")
            if check == "n" or check == "y":            #this while true loop checks to make sure the user makes a valid y/n selction.
                break                                   #otherwise the program would accept anything other then n as valid
            else:
               print ("please make a valid selection. (y/n)")

        if check == "n": #this finishes the while true loop we started at the top of the function, where the only break is input n.
            print('\nBye!')
            break        #this way, input y will break the above while true loop but not the final loop, and input n will break both.
                         #anything else will give an "invalid input" prompt.

main()
