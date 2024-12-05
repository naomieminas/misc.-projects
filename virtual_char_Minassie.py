# Virtual Character Simulator
# Naomie Minassie
# CMSC 150 - Section 04
# 10/25/2024

class Food:
    '''Food for the virtual character to eat'''
    def __init__(self, name:str, pts:int=2):
        '''Initializer function for the Food class'''
        self.name = name
        self.pts = pts

    def get_name(self):
        return self.name

    def get_pts(self):
        return self.pts

class Toy:
    '''Toy for the virtual character to play with'''
    def __init__(self, name:str):
        '''Initializer function for the Toy class'''
        self.name = name

    def get_name(self):
        return self.name


class VirtualChar:
    def __init__(self,name:str,char_type:str):
        '''Initializer function for the virtual character class'''
        self.name = name
        self.char_type = char_type
        
        self.hunger = 5
        self.max_hunger = 10
        self.mood = "neutral"

        self.moodSwing()

    def get_name(self):
        return self.name
    
    def stats(self):
        '''Prints all of the properties of the virtual character'''
        print(f"\nName: {self.name} \nType: {self.char_type} \
        \nHunger: {self.hunger}/{self.max_hunger} \nMood: {self.mood}\n")


    def eat(self,food:Food):
        '''The character eats food to restore hunger'''
        i = 0
        while (i < food.get_pts()) and (self.hunger < self.max_hunger):
            i += 1
            self.hunger += 1
        print(f"\n{self.name} ate {food.get_name()}. Restored {i} hunger!")
        self.moodSwing()

    def play(self,toy:Toy):
        '''The character plays with a toy to restore mood, but loses hunger'''
        name = self.name
        toy_name = toy.get_name()
        print(f"\n{name} used a {toy_name}.")
        self.hunger -= 1 if self.hunger != 0 else 0
        self.moodSwing()

    def moodSwing(self):        #Q8
        '''Changes the character's mood based on their hunger level'''
        if self.hunger > (self.max_hunger/2):
            self.mood = "happy"
        elif (self.max_hunger/2) >= self.hunger > (self.max_hunger/4):
            self.mood = "neutral"
        elif (self.max_hunger/4) >= self.hunger:
            self.mood = "sad"


def main():
    pet_1 = VirtualChar("Paul", "Player1")      #Q2
    pet_2 = VirtualChar("John", 'Player2')
    pet_3 = VirtualChar('George', 'Player3')
    pet_1.stats()               #Q3
    pet_2.stats()
    pet_3.stats()
    toy1 = Toy("Ringo")         #Q4
    pet_1.play(toy1)       #Q5
    food1 = Food("Apple", 3)    #Q6
    pet_2.eat(food1)            #Q7
    pet_2.stats()
    

if __name__ == "__main__":
    main()

