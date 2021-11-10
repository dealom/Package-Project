from PasswordFromScratch.Profile import *
def scratch():
    name = input("What is your full name? ")
    food = input("What is your favorite food? ")
    time = input("At what hour do you like to eat your favorite food? (Input an integer between 0 and 23) ")
    while type(time) is not int:
        try:
            time = int(time)
        except:
            print("Invalid input! Try again!")
            time = input("At what hour do you like to eat your favorite food? (Input an integer between 0 and 23) ")
    # I don't mind if the integer is actually outside the given range since it does not interfere with the program

    x = Profile(name,food,time)
    print("Here are some passwords you can use!: ")
    a = x.sentence()
    b = x.acro()
    print(a)
    print(b)

    c = input("Which password do you prefer? (Input 1 or 2) ")
    while c!="1" and c!="2":
        print("Invalid input! Try again!")
        c = input("Which password do you prefer? (Input 1 or 2) ")
    if c=="1":
        pw = a
    if c=="2":
        pw = b
    print(f"Your password is: ")
    print(pw)

    q = input("Want to try to enter your password without looking? (Input Y or N) \nWARNING: If you input Y, the terminal will be cleared!! ")
    while q!="Y" and q!="N":
        print("Invalid input! Try again!")
        q = input("Want to try to enter your password without looking? (Input Y or N) \nWARNING: If you input Y, the terminal will be cleared!! ")

    while q == "Y":
        print(chr(27) + "[2J") # clears terminal
        guess = input("Enter your password: ")
        while guess!= pw:
            print(f'Incorrect! Your password is: {pw}')
            print(f'You entered: {guess}')
            q = input(f'Would you like to try again? (Input Y or N) \nWARNING: If you input Y, the terminal will be cleared!! ')
            if q == "Y":
                print(chr(27) + "[2J")
                guess = input("Enter your password: ")
            else: # Last step so I don't mind an invalid input
                break
        print("Congrats, you correctly entered your password correctly!")
        break

    print("This is the end of the program. I hope you enjoyed using it.")
    print("Check how secure your password is at https://www.passwordmonster.com/ or https://howsecureismypassword.net/")