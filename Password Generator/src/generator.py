#Password Generator given length
import random


chars = "1234567890qwertyuiopasdfghjklzxcvbnm"
length = int(input("How long would you like your password: "))  #number of letters in password

def generatePassword(l):
    password = ''
    
    for i in range(l):
        password += random.choice(chars)
    
    return password


print ("Your password: %s" % (generatePassword(length)) )
