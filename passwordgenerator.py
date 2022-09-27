
from ast import Pass
from random import random


import random
def randomPassword():


    userInputD = (input("whats the minimum amount of digits you would like ? "))
    intUserInput = int(userInputD)
    
    userInpuUL = (input("whats the minimum amount of upper case  you would like ? "))
    intUserInputUC = int(userInpuUL)

    userInputLL = (input("whats the minimum amount of lower case letters you would like ? "))
    intUserInputLL = int(userInputLL)

    userInputSC = (input("whats the minimum amount of special characters  you would like ? "))
    intUserInputSC = int(userInputSC)



    



    lowerchars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperchars=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    specialchars=['?','>','!','<','"',':',';','{','[',']','}','|','\\','~','@','#','$','%','^','&','*','*','(',')','-','+','-','=']
    numbers=['1','2','3','4','5','6','7','8','9','0']


    
    digits = "".join(random.sample(numbers,intUserInput))
    uppercase = "".join(random.sample(upperchars,intUserInputUC))
    lowercase = "".join(random.sample(lowerchars,intUserInputLL))
    special = "".join(random.sample(specialchars,intUserInputSC))






    # rUChars = random.choice(upperchars) * intUserInputUC
    # rLChars = random.choice(lowerchars) * intUserInputLL


    # rSC = random.choice(specialchars) * intUserInputSC


    

    finalPass = digits + uppercase + lowercase + special











  







    return finalPass


def main():
    print(randomPassword())

if __name__ == "__main__":
    main()