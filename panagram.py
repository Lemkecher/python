# define the string true if panagram

import string 
def ispanagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet :
        if char not in str.lower() :
            return False 
    return True

string = input ( 'write your sentence:  ' )
if(ispanagram(string)== True) :
    print('yes')
else :
    print ('no')    