 #First virtual pet program that has limited features and doesn't use classes. 
 
 #Define a dictionary that holds our pet's attributes.
puppy_1 = {
    "name": "Cujo",
    "fullness": 50,
    "happiness": 20,
    "hunger": 7,
    "mopiness": 4,
}

puppy_2 = {
    "name": "Benji",
    "fullness": 50,
    "happiness": 100,
    "hunger": 3,
    "mopiness": 2,
}

#Define a list that holds all of our pets:
pets = [puppy_1, puppy_2]

#Each pet is adjusted individually
def get_hungry_and_mopey(pet):
    pet["fullness"] -= pet["hunger"]
    pet["happiness"] -= pet["mopiness"]

# Define functions that increase a pet's attribute levels.
def feed_pet(pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet["happiness"] += 10

# Decrease a pet's attribute levels.    
def get_hungry_and_mopey(pet):
    pet["fullness"] -= 5
    pet["happiness"] -= 5

# Prompt the user to interact with the pet
while True:

    print("""
%s's stats:
Fullness: %d
Happiness: %d
""" % (puppy_1["name"], puppy_1["fullness"], puppy_1["happiness"]))
    
    choice = int(input("""
1. Feed puppy
2. Play with puppy
3. Do nothing
"""))
    if choice == 1:
        which_pet = int(input("Which pet ?"))
        feed_pet(puppy_1)
    elif choice == 2:
        which_pet = int(input("Which pet ?"))
        play_with_pet(puppy_1)
    else:
        pass

    # Each time the loop runs, the pet
    # will need some attention!
    get_hungry_and_mopey(puppy_1)
    get_hungry_and_mopey(puppy_2) 