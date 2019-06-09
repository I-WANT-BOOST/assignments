import random

while True: #the whole program is nested in a while true statement so it's repeatable.

    def collectStringInput():
        userSelect=input('Enter [R]ock, [P]aper, or [S]cissors\nPlayer:')
        if userSelect in ("R","r","P","p","S","s"):
            return userSelect
        else:
            print("Please make a valid selection and try again. (R,r,P,p,S,s)")
        #this function gets player input and checks it against the valid selections,
        #prompting the player to try again if they mistype.
        
    def generateIntegerValue():
        randomInt = random.randint(1,6)#there are 6 valid selections, so 6 random variables.
        return randomInt

    def convertIntegerToRPS(x): 
        compSelect = ""
        if x == 1:
            compSelect = "r"
        elif x == 2:
            compSelect = "R"  #mapping each variable to a respective str selection.
        elif x == 3:
            compSelect = "p"
        elif x == 4:
            compSelect = "P"
        elif x == 5:
            compSelect = "s"
        elif x == 6:
            compSelect = "S"
        return compSelect

    def evaluateWinning(comp,user): #this function might come off a little convuluted,
        #but it's just comparing each possible player selection against the respective computer selections.
        #upper and lower case are grouped together to save space.

        if user=='r' or user=='R': #possible outcomes for a player selected Rock variable.

            if comp=='r' or comp=='R':

              print('\nTie!')

            elif comp=='p' or comp=='P':

              print('\nPaper covers rock.\nComputer WINS!')

            elif comp=='s' or comp=='S':

              print('\nRock smashes scissors.\nPlayer WINS!')



        elif user=='p' or user=='P': #possible outcomes if player selected Paper.
              
            if comp=='p' or comp=='P':

              print('\nTie!')

            elif comp=='s' or comp=='S':

              print('\nScissors cut paper.\nComputer WINS!')

            elif comp=='r' or comp=='R':

              print('\nPaper covers rock.\nPlayer WINS!')



        elif user=='s' or user=='S': #possible outcomes if player selected Scissors

            if comp=='s' or comp=='S':

              print('\nTie!')

            elif comp=='r' or comp=='R':

              print('\nRock smashes scissors.\nComputer WINS!')

            elif comp=='p' or comp=='P':

              print('\nScissors cut paper.\nPlayer WINS!')

    playerSelect = collectStringInput() 

    computerSelect = convertIntegerToRPS(generateIntegerValue())
    print("\nComputer's selection:",computerSelect) #pulling it all together, I define my player input function,
                                                    #and computer input, print the computer selection and then
                                                    #feed them into the evaluateWinning function.
    evaluateWinning(computerSelect,playerSelect)
    
    while True:
        check = input("would you like to play again? \n(y/n):")
        if check == "n" or check == "y":            #this while true loop checks to make sure the user makes a valid y/n selction.
            break                                   #otherwise the program would accept anything other then n as valid
        else:
            print ("please make a valid selection. (y/n)")
        
    if check == "n": #this finishes the while true loop we started at the top of the program, where the only break is input n.
        break        #this way, input y will break the above while true loop but not the final loop, and input n will break both.
                     #anything else will give an "invalid input" prompt.

#I know I wasn't supposed to get fancy but I was having too much fun, and it works!
