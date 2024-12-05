# Lab 3: Checking it Twice, Naomie Minassie, 9/13/24, CMSC 150 - Section 04
import random

#Question 2
naughty = ['Charlotte', 'Kai', 'Max', 'Lukas', 'Ethan']
nice = ['Nina', 'Ravi', 'Leila', 'Amara', 'Matteo', 'Yara', 'Jasper', 'Linus', \
        'Hiro', 'Aiden', "D'Arcy", 'Saoirse', 'Ralphie', 'Maya', 'Isabella']
print('\n== Q1 ==\nNICE list: ', nice , '\nNAUGHTY list: ', naughty)

#Question 3
naughty.append('Dade')
print('\n== Q3 ==\nNAUGHTY list: ', naughty)

#Question 4
nice.remove('Linus')
naughty.insert(0, 'Linus')
print('\n== Q4 ==\nNICE list: ', nice , '\nNAUGHTY list: ', naughty)

#Question 5
print('\n== Q5 ==\nNICEST KIDS: ')
for i in range(5):
    kid = nice[i]
    print("#", i+1, "-", kid)

naughtiest_kids = naughty[:3:-1]
print("\nNAUGHTIEST KIDS: ")
for i in range(3):
    kid = naughtiest_kids[i]
    print("#", i+1, "-", kid)

#Question 6
toy_catalog = ['IPhone 15 Pro', 'Red Ryder BB Gun', 'Scooter', 'LEGOs', '\
Barbie Dreamhouse', 'Tamagotchi', 'Nintendo Switch', 'Bitzee', 'PLAY-DOH', '\
Squishmallow']
print("\n== Q6 ==\nSanta's Toys: ", toy_catalog)

#Question 7

print("\n== Q7 ==")
for i in range(14):
    kid = nice[i]
    random.shuffle(toy_catalog)
    toy_list = toy_catalog[:5]
    if kid == "Ralphie":
        ralphie_list = toy_list
    else:
        ""
    print("\n", kid, " -", toy_list)
    
#Question 8
print("\n== Q8 ==")
if "Red Ryder BB Gun" in ralphie_list:
    print("\nRalphie's Original List: ", ralphie_list)
    ralphie_list.remove("Red Ryder BB Gun")
    ralphie_list.append("Football")
    print("\nRalphie's New, Mom-Approved List: ", ralphie_list)
else:
    print("Ralphie did not get a Red Ryder BB Gun.")

