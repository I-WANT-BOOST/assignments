import random
print('Welcome to my Tamagotchi program! In it, you will take care of your Tamagotchi by feeding or playing.\n'
'Every round, happiness and hunger will decrease by one.\nIf you over feed your Tamagotchi (by feeding past 10/10),they will get sick.\n'
'The ammount you feed them past 10 is the ammount of sickness they will gain.\n'
'There is no way to decrease sickness. If Hunger or Happiness reach 0/10 or Sickness reaches 10/10, your Tamagotchi will die.\n'
'Feeding increases hunger by 2, and playing increases happiness by 3.\nYou cannot over fill happiness.\n'
'There are several different Tamagotchi types with different needs.\nAll stats are out of 10 unless otherwise noted.\n'
'Good luck and have fun!\n\n')
while True:
    typeChoice = input('Choose a Tamagotchi type:\n (Normal, Fancy, Plant, or Hungry)\n>')
    validTypeChoice = ['normal','Normal','fancy','Fancy','plant','Plant','hungry','Hungry']
    if typeChoice not in validTypeChoice:
        print('Please make a valid Type choice')
    else:
        break
nam = input('\nName your Tamagotchi!:')

class tamagotchi:
    name = ''
    gender = ''
    characterType = ''
    hunger = int()
    happiness = int()
    sickness = int()
    count = int()
    specialCount = -1
    genderBinary = int()
    characterBinary = int()

    def __init__(self, nam): #swol Tamagotchi?
        self.name = nam
        self.hunger = 11
        self.happiness = 11
        self.sickness = 0
        self.genderBinary = random.randint(0,1)
        self.characterBinary = random.randint(1,5)
        self.specialCount = 0

    def genderSelect(self):
        if self.genderBinary == 0:
            self.gender = 'She'
        elif self.genderBinary == 1:
            self.gender = 'He'

    def characterSelectNorm(self):
        if self.characterBinary == 1:
            self.characterType = 'Happy'
        elif self.characterBinary == 2:
            self.characterType = 'Shy'
        elif self.characterBinary == 3:
            self.characterType = 'Aggressive'
        elif self.characterBinary == 4:
            self.characterType = 'Energetic'
        elif self.characterBinary == 5:
            self.characterType = 'Friendly'

    def normalBorn(self):
        print('\nYour Tamagotchi is born!')
        print (self.name,'is a',self.characterType,'Tamagotchi.\n',self.gender,'was born healthy.')

    def turn(self):
        self.hunger = self.hunger - 1
        self.happiness = self.happiness - 1
        self.count = self.count + 1
        self.specialCount = self.specialCount + 1

    def status(self):
        print('\n',self.name,"'s Stats are:\nHunger:",self.hunger,'\nHappiness:',self.happiness,'\nSickness:',self.sickness,)

    def feedNorm(self):
        self.hunger = self.hunger + 3
        if self.hunger > 11:
            self.sickness = self.sickness + (self.hunger-11)
            self.hunger = 11
            print('Be careful not to over feed your Tamagotchi!\nSickness:',self.sickness,)

    def play(self):
        self.happiness = self.happiness + 4
        if self.happiness > 11:
            self.happiness = 11

def normalTam():
    print('\nYou selected a Normal Tamagotchi!\nNormal Tamagotchi require no special care.\nJust feed them,'
    "play with them, and make sure they don't get sick!")
    norm = tamagotchi(nam)
    norm.genderSelect()
    norm.characterSelectNorm()
    norm.normalBorn()
    while True:
        norm.turn()
        norm.status()
        validChoice = ['feed','Feed','play','Play','wait','Wait','quit','Quit']
        if norm.hunger <= 0 or norm.happiness <= 0 or norm.sickness >= 10:
            print('Your Tamagotchi has died.\nThey lasted',norm.count,'turns.')
            break
        choice = input('What would you like to do next? (Feed, Play, Wait, or Quit)\n>')
        if choice not in validChoice:
            print('Please make a valid selection. (Feed, Play, Wait, or Quit)')
        elif choice.lower() == 'feed':
            norm.feedNorm()
        elif choice.lower() == 'play':
            norm.play()
        elif choice.lower() == 'quit':
            break

class fancyTamagotchi(tamagotchi):
    hair = int()

    def __init__(self,nam):
        super().__init__(nam)
        self.hair = 11

    def turn(self):
        super().turn()
        self.hair = self.hair - 1
        if self.hair == 0:
            self.happiness = self.happiness - 1

    def status(self):
        super().status()
        print('Hair:',self.hair,)

    def groom(self):
        self.hair = self.hair + 6
        if self.hair > 11:
            self.hair = 11

def fancyTam():
    print('\nYou selected a Fancy Tamagotchi!\nFancy Tamagotchi have a fancy hair cut that you must maintain\nFeed them,'
    "play with them, and make sure they don't get sick!\n"
    'You must also groom them, if their haircut reaches 0/10, happiness will go down twice as fast!')
    fancy = fancyTamagotchi(nam)
    fancy.genderSelect()
    fancy.characterSelectNorm()
    fancy.normalBorn()
    while True:
        fancy.turn()
        fancy.status()
        validChoice = ['feed','Feed','play','Play','wait','Wait','quit','Quit','groom','Groom']
        if fancy.hunger <= 0 or fancy.happiness <= 0 or fancy.sickness >= 10:
            print('Your Tamagotchi has died.\nThey lasted',fancy.count,'turns.')
            break
        choice = input('What would you like to do next? (Feed, Play, Wait, Groom, or Quit)\n>')
        if choice not in validChoice:
            print('Please make a valid selection. (Feed, Play, Wait, or Quit)')
        elif choice.lower() == 'feed':
            fancy.feedNorm()
        elif choice.lower() == 'play':
            fancy.play()
        elif choice.lower() == 'groom':
            fancy.groom()
        elif choice.lower() == 'quit':
            break

class plantTamagotchi(tamagotchi):
    def __init__(self,nam):
        super().__init__(nam)
        self.hunger = 21

    def turn(self):
        super().turn()
        if self.specialCount > 10:
            self.sickness = self.sickness + 1
            print('\n',self.name,'is Wilted!\nFeed them so they stop getting sick!')

    def status(self):
        super().status()
        print('Turns without being fed:',self.specialCount,)

    def characterSelectPlant(self):
        if self.characterBinary == 1:
            self.characterType = 'Radiant'
        elif self.characterBinary == 2:
            self.characterType = 'Crooked'
        elif self.characterBinary == 3:
            self.characterType = 'Wind Swept'
        elif self.characterBinary == 4:
            self.characterType = 'Droopy'
        elif self.characterBinary == 5:
            self.characterType = 'Thriving'

    def plantBorn(self):
        print('\nYour Tamagotchi has bloomed!')
        print (self.name,'is a',self.characterType,'Tamagotchi.\nThey bloomed healthy.')

    def feedPlant(self):
        self.hunger = self.hunger + 3
        self.specialCount = -1
        if self.hunger > 21:
            self.sickness = self.sickness + (self.hunger-21)
            self.hunger = 21
            print('Be careful not to over feed your Tamagotchi!\nSickness:',self.sickness,)

def plantTam():
    print('\nYou selected a Pant Tamagotchi!\nPlant Tamagotchi have photosynthesis, so they have double hunger!'
    "\nBut, if you don't feed you Plant Tamagotchi for 10 turns, They will get wilted.\nEvery turn that they are wilted, they will gain one sickness."
    "\nJust feed them,play with them, and make sure they don't get sick!")
    plant = plantTamagotchi(nam)
    plant.genderSelect()
    plant.characterSelectPlant()
    plant.plantBorn()
    while True:
        plant.turn()
        plant.status()
        validChoice = ['feed','Feed','play','Play','wait','Wait','quit','Quit']
        if plant.hunger <= 0 or plant.happiness <= 0 or plant.sickness >= 10:
            print('Your Tamagotchi has died.\nThey lasted',plant.count,'turns.')
            break
        choice = input('What would you like to do next? (Feed, Play, Wait, or Quit)\n>')
        if choice not in validChoice:
            print('Please make a valid selection. (Feed, Play, Wait, or Quit)')
        elif choice.lower() == 'feed':
            plant.feedPlant()
        elif choice.lower() == 'play':
            plant.play()
        elif choice.lower() == 'quit':
            break

class hungryTamagotchi(tamagotchi):
    def __init__(self,nam):
        super().__init__(nam)
        self.hunger = 16

    def turn(self):
        super().turn()
        if self.specialCount > 6:
            self.happiness = self.happiness - 1
            print('\n',self.name,"Hasen't had their belly rub!\nGive them a belly rub so they don't loose happiness!")

    def status(self):
        super().status()
        print('Turns without belly rub:',self.specialCount)

    def feedHungry(self):
        self.hunger = self.hunger + 3
        if self.hunger > 16:
            self.sickness = self.sickness + (self.hunger-16)
            self.hunger = 16
            print('Be careful not to over feed your Tamagotchi!\nSickness:',self.sickness,)

    def bellyrub(self):
        self.specialCount = -1

def hungryTam():
    print('\nYou selected a Hungry Tamagotchi!\nHungry Tamagotchi have 15 hunger!\nFeed them,'
    "play with them, and make sure they don't get sick!\n"
    "You must also give them belly rubs, if you don't for more then 5 turns,\nHappiness will go down twice as fast!")
    hungry = hungryTamagotchi(nam)
    hungry.genderSelect()
    hungry.characterSelectNorm()
    hungry.normalBorn()
    while True:
        hungry.turn()
        hungry.status()
        validChoice = ['feed','Feed','play','Play','wait','Wait','quit','Quit','bellyrub','Bellyrub']
        if hungry.hunger <= 0 or hungry.happiness <= 0 or hungry.sickness >= 10:
            print('Your Tamagotchi has died.\nThey lasted',hungry.count,'turns.')
            break
        choice = input('What would you like to do next? (Feed, Play, Wait, Bellyrub, or Quit)\n>')
        if choice not in validChoice:
            print('Please make a valid selection. (Feed, Play, Wait, Bellyrub or Quit)')
        elif choice.lower() == 'feed':
            hungry.feedHungry()
        elif choice.lower() == 'play':
            hungry.play()
        elif choice.lower() == 'bellyrub':
            hungry.bellyrub()
        elif choice.lower() == 'quit':
            break


if typeChoice.lower() == 'normal':
    normalTam()
if typeChoice.lower() == 'fancy':
    fancyTam()
if typeChoice.lower() == 'plant':
    plantTam()
if typeChoice.lower() == 'hungry':
    hungryTam()
