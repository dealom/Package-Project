class Pword: # I want to use certain variables between functions so I'm using a class only for that.
    def __init__(self,pw):
        self.pw = pw

    def checklist(self):
        self.huge = False # at least 8 chars
        self.both = False # both upper and lower
        self.nums = False # both letters and numbers
        self.spec = False # includes a special character
        cool = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        if len(self.pw)>=8:
            self.huge = True
        self.up = False # has uppercase letter
        self.lo = False # has lowercase letter
        self.nu = False # has number
        self.ms = False # has letter
        for c in self.pw:
            if c.isnumeric():
                self.nu = True
            if c.isalpha():
                self.ms = True
            if c in cool:
                self.spec = True
            if c.isupper() == True:
                self.up = True
            if c.islower() == True:
                self.lo = True
        if self.up and self.lo:
            self.both = True
        if self.nu and self.ms:
            self.nums = True
        
        if self.huge and self.both and self.nums and self.spec:
            feedback = "Your password is good."
            good = True
        else:
            feedback = "Your password is not good. It should meet all requirements listed above. "
            good = False
        # I want a boolean for good/bad and I want to print feedback
        print(f'At least 8 characters: {self.huge}\nHas both uppercase and lowercase letters: {self.both}\nHas numbers and letters: {self.nums}\nHas special characters: {self.spec}\n{feedback}\n')
        return good

    def fix(self): # Aa1!Aa1!
        # at least 8 chars, upper and lowercase, letters and numbers, one special character
        if self.up == False:
            self.pw += 'A'
        if self.lo == False:
            self.pw += 'a'
        if self.nu == False:
            self.pw += '1'
        if self.spec == False:
            self.pw += '!'
        if self.huge == False:
            self.pw *= 2
        return self.pw