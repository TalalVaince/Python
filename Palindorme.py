def reverse(f): #used for the purpose to learn the def function (i know how to do without this function) 
    ''' This function gives the reverse of a string'''
    return f[::-1]
def palindorme(s):
    ''' This function recognizes if the word is a palindorme'''
    if len(s) == 1:
        return False
    else:
        if reverse(s) == s:
            return True 
        else:
            return False
word = input("Enter Your Word: ")
if (palindorme(word)==True):
    print ("Your word is a palindrome")
else:
    print ("Your Word isn't a palindrome")