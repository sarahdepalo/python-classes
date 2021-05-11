class Cat:
    #Class attribute
    species = "mammal"
    
    #Constructor:
    def __init__(self, name, age):
        self.name = name #Every cat that we make is going to have a name and an age.
        self.age = age # You always have to have the 'self' parameter in the constructor. 
    def describe(self):
        return "%s is %d years old" % (self.name, self.age)

#The only arguments that Cat is expecting is 'name' and 'age'
guster = Cat("Guster", 11)
bandit = Cat("Bandit",11)

print(guster.describe())
print(bandit.describe())