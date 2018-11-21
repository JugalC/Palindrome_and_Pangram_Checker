from Palindrome import *
from Pangram import *

userchoice = input("Type 1 for Palindrome check or type 2 for Pangram check: ")
userstring = input("Type the word or phrase you want to check? ")

if userchoice == "1":
    pal(userstring)
if userchoice == "2":
    pan(userstring)
