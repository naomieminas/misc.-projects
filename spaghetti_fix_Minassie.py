# SPAGHETTI CODE
# Written by ChatGPT + A naive programmer
# Fixed by Naomie Minassie
# November 8, 2024
# CMSC 150 - Section 04


import math
import random
from operator import index

"""

 /$$$$$$$              /$$     /$$                          
| $$__  $$            | $$    | $$                          
| $$  \ $$ /$$   /$$ /$$$$$$  | $$$$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$/| $$  | $$|_  $$_/  | $$__  $$ /$$__  $$| $$__  $$
| $$____/ | $$  | $$  | $$    | $$  \ $$| $$  \ $$| $$  \ $$
| $$      | $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$  | $$
| $$      |  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$/| $$  | $$
|__/       \____  $$   \___/  |__/  |__/ \______/ |__/  |__/
           /$$  | $$                                        
          |  $$$$$$/                                        
           \______/ 
"""


def is4Mult(n):
    """Checks if a number is a multiple of 4"""
    return True if n % 4 == 0 else False

def print10(l:list):
    """Prints items in a list on separate lines up to the first 10"""
    [print(i) for i in l[:10]]

def sameArr(a,b):
    """Checks if 2 1-dimensional arrays are the same"""
    return True if a == b else False

class Car:
    """A car class for driving"""
    def __init__(self, year:int, make:str, model:str):
        self.year = year
        self.make = make
        self.model = model

    def start_engine(self):
        """Starts the engine"""
        print("Engine started")

    def drive(self):
        """Shows what kind of car is being driven"""
        print(f"I'm driving a {self.year} {self.make} {self.model}.")

def calculate_total(prices:list):
    """Gets the total of a list of prices"""
    return sum(prices)

def square(l:list):
    """Squares each number in a list l"""
    return [pow(n, 2) for n in l]

def isOk(a:str):
    """Checks if a string is 'Ok'"""
    return True if a == "Ok" else False

def find_max(numbers:list):
    """Returns the maximum value in a list of numbers"""
    return max(numbers)

def changeAllT(b:list):
    """Returns an array where all letter t's in a list of strings are changed to the letter o"""
    return [i.replace('t', 'o') for i in b]

def lucky7():
    """Randomly generate 2 numbers from range 1-6
        Print the sum of the dice
        If they add to 7, return "win" and "lose" if otherwise"""
    dice1 = random.randint(0,6)
    dice2 = random.randint(0,6)
    print(f"{dice1} + {dice2} = {dice1 + dice2}")
    return "win" if dice1 + dice2 == 7 else "lose"

def onlyT(c:list):
    """Returns items in a string list that have a 't' in it"""
    return [word for word in c if 't' in word]


# DO NOT CHANGE ANYTHING BELOW #

if __name__ == "__main__":

    print("== is4Mult() ==");print(is4Mult(5));print(is4Mult(16))

    print("\n== print10() ==");print10(['a','b','c','d','e','f','g'])

    print("\n== sameArr() ==");print(sameArr(['red','blue'],['gold','black']));print(sameArr(['a'],['a','r','e']));print(sameArr([420,69],[420,69]))

    print("\n== Car.drive() ==");my_car = Car(2017, "Nissan", "Sentra");my_car.start_engine();my_car.drive()

    print("\n== calculate_total() ==");print(calculate_total([10, 20, 30]))

    print("\n== square() ==");numbers = [1, 2, 3, 4, 5];print(square(numbers))

    print("\n== isOk() ==");print(isOk("Ok"));print(isOk("not ok"))

    print("\n== find_max() ==");print(find_max([8,10,3000,128,32.023]))

    print("\n== changeAllT() ==");print(changeAllT(["don't",'try','to','allow','another','error']))

    print("\n== lucky7() ==");print(lucky7());print(lucky7());print(lucky7())

    print("\n== onlyT =="); print(onlyT(['That','game','is','totally','cool','Trevor']))
        
