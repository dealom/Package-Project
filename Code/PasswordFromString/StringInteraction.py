from PasswordFromString.StringChecklist import *
from PasswordFromString.StringFunctions import *
def improve():
    pw = input("Enter your password: ")
    password = Pword(pw)
    g = password.checklist()
    if g == False:
        print("Fixing your password...")
        pw = password.fix()
        print(f'Your new password is: {pw}')
        print("Your new password fulfills the common password requirement shown below.")
        npw = Pword(pw)
        g = npw.checklist()
    
    if g == True:
        c = input("Your password may contain easy to guess English words. Would you like to alter the letters in your password? (Input Y or N) ")
        while c!="Y" and c!="N":
            print("Invalid input! Try again!")
            c = input("Your password may contain easy to guess English words. Would you like to alter the letters in your password? (Input Y or N) ")
        if c=="Y":
            print("Would you like to shift the letters:")
            print("(1) Alphabetically, meaning: a -> b, b -> c, p -> q")
            print("(2) Based on keyboard placement, meaning: a -> s, s -> d, q -> w")
            f = input("Input 1 or 2: ")
            while f!="1" and f!="2":
                print("Invalid input! Try again!")
                f = input("Input 1 or 2: ")
            if f=="1":
                print("Enter a positive or negative integer representing the amount of letters to shift by.")
                print("For example, entering -3 will change \'p\' to \'m\' and entering 2 will change \'p\' to \'r\'. ")
                ashift = int(input("Enter an integer: "))
                anewpw = alpharight(pw,ashift)
                print(f"Your new password is: {anewpw}")
            elif f=="2":
                print("Enter a positive or negative integer representing the amount of letters to shift by.")
                print("For example, entering -3 will change \'p\' to \'u\' and entering 2 will change \'p\' to \'s\'. ")
                kshift = int(input("Enter an integer: "))
                knewpw = keyright(pw,kshift)
                print(f"Your new password is: {knewpw}")

        

    print("This is the end of the program. I hope you enjoyed using it.")
    print("Check how secure your password is at https://www.passwordmonster.com/ or https://howsecureismypassword.net/")