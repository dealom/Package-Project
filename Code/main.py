
from PasswordFromString.StringChecklist import *
from PasswordFromString.StringFunctions import *
from PasswordFromString.StringInteraction import *
from PasswordFromScratch.Profile import *
from PasswordFromScratch.ScratchInteraction import *

print("Hello. This program is a password generator that helps you create a password that is both memorable and secure.") 
path = input("Do you want to create a new password from scratch (1) or improve a current password (2)? ")

while path != "1" and path != "2":
    print("Invalid Input")
    path  = input("Do you want to create a new password from scratch (1) or improve a current password (2)? ")

if path == "1":
    scratch()

if path == "2":
    improve()


