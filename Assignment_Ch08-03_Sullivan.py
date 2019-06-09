inStock = [[],[],[],[],[],[],[],[],[],[]]
gamma = [11,13,15,17]
delta = [3,5,2,6,10,9,7,11,1,8]
from copy import deepcopy

def setZero():
    alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    beta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print('Alpha after initialization:\n',alpha)
    return (alpha,beta)
alpha,beta = setZero()

def inputArray():
    alpha = []
    print('Enter 20 integers:')
    for i in range(1,21):
        number = int(input('{}:'.format(i)))
        alpha.append(int(number))
    return alpha
alpha = inputArray()

def doubleArray(alpha,beta):
    beta = []
    for i in alpha:
        beta.append(i*2)
    return beta

def copyGamma(newInStock,gamma):
    newInStock[0] = gamma
    num1 = gamma[0]
    num2 = gamma[1]
    num3 = gamma[2]
    num4 = gamma[3]
    for i in range(1,10):
        num1 = num1*3
        newInStock[i].append(num1)
        num2 = num2*3
        newInStock[i].append(num2)
        num3 = num3*3
        newInStock[i].append(num3)
        num4 = num4*3
        newInStock[i].append(num4)
    return newInStock

def copyAlphaBeta(alpha,beta):
    inStock = alpha + beta
    return inStock

def printArray(alpha,beta):
    print ('\nAlpha after reading 20 numbers:\n',alpha[0:10],'\n',alpha[10:20])
    print ('\nBeta after a call to doubleArray:\n',beta[0:10],'\n',beta[10:20])

def setInStock(inStock,delta):
    print('\nEnter 10 integers:')
    for i in range(10):
        num1 = int(input(''))
        inStock[i].append(num1)
        num2 = (num1*2)-(delta[i])
        inStock[i].append(num2)
        num3 = (num2*2)-(delta[i])
        inStock[i].append(num3)
        num4 = (num3*2)-(delta[i])
        inStock[i].append(num4)
    return inStock

beta = doubleArray(alpha[:],beta[:])
newInStock = deepcopy(inStock)
copyGamma = copyGamma(newInStock,gamma[:])
copyAlphaBeta = copyAlphaBeta(alpha[:],beta[:])

printArray(alpha,beta)
print ('\ninStock after a call to copyGamma:\n',copyGamma,sep=('\n'))
print ('\ninStock after a call to copyAlphaBeta:\n',copyAlphaBeta,)

setInStock = setInStock(inStock[:],delta)
print ('\ninStock after a call to setInStock:\n',setInStock)
