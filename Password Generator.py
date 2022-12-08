# 1- import string and random modules
# 2- store all characters in lists (upper/lower case, digists, punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digits and punctuations

print(" _____                             _    _____                     _           ")
print("|  _  | __ ___ ___ _ _ _ ___ ___ _| |  |   __|___ ___ ___ ___  __| |_ ___ ___ ")
print("|   __||. |_ -|_ -| | | | . |  _| . |  |  |  | -_|   | -_|  _||. |  _| . |  _|")
print("|__|  |___|___|___|_____|___|_| |___|  |_____|___|_|_|___|_| |___| | |___|_|  ")
print("                                                                 |__|         ")

import random
import string

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
digits = list(string.digits)
symbols = list(string.punctuation)

chars_number = input("Enter the number of characters: ")

#characters are 6 or more or not
while True :
    try:
        chars_number = int(chars_number)

        if chars_number < 6 :
            print("Number of characters is small /n")
            chars_number = input("Please, Enter a number more than or equal 6 : ")
        else:
            break
    
    except:
        chars_number = input("Please, Enter numbers only: ")

#shuffling the characters
random.shuffle(upper)
random.shuffle(lower)
random.shuffle(digits)
random.shuffle(symbols)

_30 = round(chars_number * 30/100) #30% upper and 30% lower = 60%
_20 = round(chars_number * 20/100) #20% digits and 20% symbols = 40%

password = []

for i in range(_30) :
    password.append(upper[i]) #30% upper added to password list
    password.append(lower[i]) #30% lower added to password list

for i in range(_20) :
    password.append(digits[i]) #20% digits added to password list
    password.append(symbols[i]) #20% symbols added to password list

random.shuffle(password)

password = "".join(password[0:]) #make the characters in the list be combined and attached

print(password)