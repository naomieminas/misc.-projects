# CHEF'S KITCHEN SIMULATION

# SIMULATION VARIABLES
MARKET = ["sugar", "egg", "milk", "flour", "butter", "cheese", "tomato", \
          "potato"]
kitchen = {}
recipes = {}

# SIMULATION LOOP
while True:
    print("Enter a command [buy, cook, show, quit]:")
    user_in = input(" > ").lower()

    # quit the game
    if user_in == "quit":
        break

    # buy ingredients and add to the kitchen
    if user_in.startswith("buy"):
        ingr = user_in.split(" ")[1:]

        # show the market options if not in stock
        for i in ingr:
            if i not in MARKET:
                x = i
                if x.isnumeric() == True and int(x) > 1 and key in kitchen:
                    kitchen[key] += ((int(x))-1)
                else:
                    print(f"{ingr} not in stock!")
                    print("You can buy: ")
                    for i in MARKET:
                        print(f"- {i}")
                
        # otherwise, add to the kitchen
            elif i in MARKET and i not in kitchen:
                key = i
                kitchen.update({key:1})

            elif i in MARKET and i in kitchen:
                kitchen[i] += 1

            else:
                kitchen[i] = 0
            
    # show the non-zero ingredients in the ktichen
    elif user_in == "show":
        print("\n==== KITCHEN ====")
        for k,v in kitchen.items():
            if v != 0:
                print(f"{k.upper()}: {v}")
        print("============\n")

    # make recipes with the ingredients
    elif user_in.startswith("cook"):
        ingr = user_in.split(" ")[1:]

        # check if all ingredients in the kitchen
        has_ingr = True
        for i in ingr:
            if i not in kitchen or kitchen[i] == 0:
                print(f"No {i} in the kitchen...")
                has_ingr = False
                break

        # make the recipe if the ingredients are there
        if has_ingr:
            cook_items = set(ingr)
            new_recipe = True

            # check if already a recipe
            for k,v in recipes.items():
                if v == cook_items:
                    print(f"Made [{k}]!")
                    new_recipe = False
                    break

            # create a new recipe if not
            if new_recipe:
                print("New recipe discovered!")
                name = input("Give it a name: ")
                recipes[name] = cook_items

            # remove the ingredients
            for i in cook_items:
                kitchen[i] -= 1



# FINAL STATS
print("==== FINAL STATS ====")

# show the ingredients left in the kitchen
tot_ingr = sum(list(kitchen.values()))
print(f"\n** Kitchen ({tot_ingr} ingredients) **")
for i,n in kitchen.items():
    print(f"{i.upper()}: {n}")

# show the recipes made
tot_rec = len(recipes)
print(f"\n** Recipes ({tot_rec} recipes made) **")
for r,c in recipes.items():
    print(f"- {r}: {c}")
        
                
