#Second version of the digital pet game that takes advantage of classes and therefore is more functional and has more capabilities.

#Define the Pet class:

class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name  = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
    
    def eat_food(self):
        self.fullness += 30
    
    def get_love(self):
        self.happiness += 30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

#Creates a subclass of Pet for naturally happier pets:
class CuddlyPet(Pet):
    pass

#List that holds all of our pets:
pets = []

#Start the game:
running = True

# while True:
#     print("""
#           %s's stats:
#           Fullness: %d
#           Happiness: %d
#           """ % (self.name, self.fullness, self.happiness))
 



#Create an instance of a class:
carmine = Pet("Carmine", 50, 20) #you can preset attributes like this that will change the defaults above. 
print(carmine.name)
carmine.eat_food()
carmine.get_love()
#Checks that be_alive is functioning correctly
carmine.be_alive()
print(carmine.fullness)
print(carmine.happiness)
anderson = Pet("Anderson")
print(anderson.name)
anderson.get_love()
anderson.eat_food()
print(anderson.fullness)
print(anderson.happiness)
