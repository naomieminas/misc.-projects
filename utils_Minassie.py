# Lab 4: Something Useful, Naomie Minassie, 09/27/2024, CMSC 150 - Section 04

import random
import math

def shuffle(arr:list):
    '''Shuffles the given list and returns it in a different order.'''
    
    x = arr.copy()
    random.shuffle(x)
    return x


def pickN(arr:list, n = 1):
    '''Shuffles the given list and returns n distinct elements of the list.'''
    
    if n <= 0:
        print("n must be greater than 0")
        return None
    elif n > len(arr):
        print("n exceeds the length of the list given")
        return None
    else:
        random.shuffle(arr)
        q = []
        while len(q) < n:
            new = random.choice(arr)
            if new not in q:
                q.append(new)
        return q

def spamChat(s:str):
    '''Repeats a given string, producing an output up to 500 characters.'''
    
    if not s:
        print("No string given!")
    else:
        while len(s) <= 500:
            s += s
        print(s)

def diceRoll(n:int, d:int):
    '''Rolls a dice from 1 to d, n times--adding the sum if n > 1.'''
    
    s = 0
    if d < 1 or n < 1:
        print("Invalid inputs. Neither d nor n can be less than 1.")
        return 0
    else:
        for i in range(n):
            a = random.randint(1, d)
            s += a
        return s

def keySwap(d:dict):
    '''Returns a new dictionary with the swapped keys and values of d.'''
    
    x = {value:key for key, value in d.items()}
    return x

def wordCts(s:str):
    '''Returns a dictionary with each word of the given string and its \
        count.'''
    
    a = s.split(" ")
    x = {}
    if not s:
        print("s cannot be empty!")
        return None
    else:
        for word in a:
            x[word] = a.count(word)
        return x







if __name__ == "__main__":
    pass
