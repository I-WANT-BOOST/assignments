inputYear = input('Enter a year between 1000 and 3000:\n')

def returnRomanThousandsPlace(x):
    if int(x)>3000:
        print('Please enter a year under 3000.')
    else:
        thousands = int(x)//1000
        thousands = thousands*'M'
        return thousands

thoPl = returnRomanThousandsPlace(inputYear)

def returnRomanHundredsPlace(x):
    hundreds = int(x)%1000
    hundreds = hundreds//100
    if hundreds == 0:
        hundreds = ''
    elif hundreds == 9:
        hundreds = 'CM'
    elif hundreds == 8:
        hundreds = 'DCCC'
    elif hundreds == 7:
        hundreds = 'DCC'
    elif hundreds == 6:
        hundreds = 'DC'
    elif hundreds == 5:
        hundreds = 'D'
    elif hundreds == 4:
        hundreds = 'CD'
    elif hundreds == 3:
        hundreds = 'CCC'
    elif hundreds == 2:
        hundreds = 'CC'
    elif hundreds == 1:
        hundreds = 'C'
    return hundreds

hunPl = returnRomanHundredsPlace(inputYear)
    
def returnRomanTensPlace(x):
    tens = int(x)%100
    tens = tens//10
    if tens == 0:
        tens = ''
    elif tens == 9:
        tens = 'XC'
    elif tens == 8:
        tens = 'LXXX'
    elif tens == 7:
        tens = 'LXX'
    elif tens == 6:
        tens = 'LX'
    elif tens == 5:
        tens = 'L'
    elif tens == 4:
        tens = 'XL'
    elif tens == 3:
        tens = 'XXX'
    elif tens == 2:
        tens = 'XX'
    elif tens == 1:
        tens = 'X'
    return tens

tenPl = returnRomanTensPlace(inputYear)

def returnRomanOnesPlace(x):
    ones = int(x)%10
    if ones == 0:
        ones = ''
    elif ones == 9:
        ones = 'IX'
    elif ones == 8:
        ones = 'VIII'
    elif ones == 7:
        ones = 'VII'
    elif ones == 6:
        ones = 'VI'
    elif ones == 5:
        ones = 'V'
    elif ones == 4:
        ones = 'IV'
    elif ones == 3:
        ones = 'III'
    elif ones == 2:
        ones = 'II'
    elif ones == 1:
        ones = 'I'
    return ones

onePl = returnRomanOnesPlace(inputYear)    

print(thoPl+hunPl+tenPl+onePl)


