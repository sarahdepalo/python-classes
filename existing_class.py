
class Person:
    def __init__(self, name, email, phone, number_of_greetings=0):
      self.name = name
      self.email = email
      self.phone = phone
      self.friends = []
      self.number_of_greetings = number_of_greetings
      self.list_of_greetings = []
      #If this was changed to return, it would no longer print each time.
      print("%s's email is %s and their phone number is %s." % (self.name, self.email, self.phone))

    #Displays a greeting and counts them
    def greet(self, other_person):
        self.number_of_greetings += 1
        #Check if unique with an if not statment!
        if other_person.name not in self.list_of_greetings:
            self.list_of_greetings.append(other_person.name)
        #Greets people and displays how many people they have greeted.
        print("Hello %s, I'm %s!" % (other_person.name, self.name))
        print("%s has greeted %d people" % (self.name, self.number_of_greetings))
        
      #Checks that the greeting is being added:
        #print(self.list_of_greetings) 

    #Prints out contact info
    def print_contact_info(self):
        print("%s's email: %s" % (self.name, self.email))
        print("%s's phone number: %s" % (self.name, self.phone))
    
    #Adds friends to the friends list    
    def add_friend(self, other_person):
        return self.friends.append(other_person)
    
    #Prints out number of friends in the friends list
    def num_friends(self):
        print("%s has %d friend(s)." % (self.name, len(self.friends)))
    
    #Prints out the number of unique_people_greeted:
    def num_unique_people_greeted(self):
        print("The number of unique people greeted is %d" % (len(self.list_of_greetings)))
    
    #Sets the standard format when each person is printed
    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.phone, self.email)
    


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
deean = Person("Deean", "deean@aol.com", "301-444-555")
sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(deean)
jordan.greet(sonny)
#jordan.number_of_greetings

#Test of the print_contact_info function:
# sonny.print_contact_info()
# #appends friends to jordan's friends list
jordan.add_friend(sonny)
#Test that the friend was actually added
#jordan.num_friends()

#Will print the contact as defined by the __str__ method
#print(jordan)

jordan.num_unique_people_greeted()

#Prints the year, make, and model of a car
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def print_info(self):
#         print("%d %s %s" % (self.year, self.make, self.model))
    
# car = Vehicle("Jeep", "Wrangler", 2014)
# car.print_info()
