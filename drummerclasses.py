class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
        print(self.sounds[i % len(self.sounds)],end=" ")
            print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bang", "Bong", "Splash"])
    
    def count(self):
        counter = 
        while (counter <= 4):
            if n =< 4
            print(count)
            count = count + 1
    
    def loud(self):
        print(spontaneously combust)
    
    
class Band(Musician):    
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__("playing","hiring","firing")
        
    def hiring(self):
        print("Talented, creative, hardworking")
        print("Your hired")
        
    def firing(self):
        print("Lazy, unproductive, disinterested")
        print("Your fired")
        
        
        
        
        
        
        
        
        