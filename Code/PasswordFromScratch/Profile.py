class Profile:
    def __init__(self,n,f,t):
        self.name = n.title() # ensures that both passwords have both upper and lower case letters
        self.food = f.title()
        self.time = t
        self.Sentence = self.sentence()
    
    def sentence(self):
        if self.time == 0:
            return (f'{self.name} likes to eat {self.food} at 12am!')
        elif self.time < 12:
            return (f'{self.name} likes to eat {self.food} at {self.time}am!')
        elif self.time == 12:
            return (f'{self.name} likes to eat {self.food} at 12pm!')
        else:
            minus12 = self.time - 12
            return (f'{self.name} likes to eat {self.food} at {minus12}pm!')

    def acro(self):
        nym = ""
        words = list(self.Sentence.split(" "))
        for word in words:
            if word == "to":
                nym += "2"
            elif word == "at":
                nym += "@"
            elif word == words[-1]:
                nym +=word[:-1]
            else:
                nym += word[0]
        return nym
