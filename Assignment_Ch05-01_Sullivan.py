evens = 0
odds = 0
numberOfInputs = 0

while True:
    
    print("input 10 numbers:")

    while True:
        
        try:
            inputList = int(input())

            numberOfInputs = numberOfInputs + 1

            if inputList % 2 == 0:
                evens = evens + inputList

            else:
                odds = odds + inputList

            if numberOfInputs == 10:
                break

        except:
            print("Please enter a number.")
            continue
        

    print("evens:",evens)
    print("odds:",odds)

    while True:
        repeat = input("would you like to play again? \n(y/n):")
        if repeat == "n" or repeat == "y":            
            break                                   
        else:
            print ("please make a valid selection. (y/n)")

    if repeat == "n":
        break
print("Done!")
