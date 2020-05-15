class Cattle(object):
    def __init__(self, animal_type, name, gender):
        self.animal_type = animal_type
        self.name = name
        self.gender = gender
        self.graze = None
        self.milk = 0
        self.feed = 0
        self.energy = 0

    def cattle_graze(self):
        if self.energy > 20:
            print("Overeating!")
        else:
            self.energy += 5
            print("energy +5!!!")
    
    def cattle_milk(self):
        if self.gender == 'female':
            if self.energy >= 10:
                self.milk += 10
                self.energy -= 5
                print("milk +10!!!")
            elif self.energy >= 5:
                self.milk += 5
                self.energy -= 5
                print("milk +5!!!")
            else:
                print("Not eaten well. No milk today")

cow1 = Cattle("Cow", "anthony", "male")
cow2 = Cattle("Cow", "jerome", "female")
cow3 = Cattle("Cow", "delaney", "female")

while True:

    action = input(("g to graze, m to milk cattle: "))
    if action == 'g':
        namey = input("Whom to feed: ")
        if namey == "cow1":
            cow1.cattle_graze()
        if namey == "cow2":
            cow2.cattle_graze()
        if namey == "cow3":
            cow3.cattle_graze()
    elif action == 'm':
        namey = input("Whom to milk: ")
        if namey == "cow1":
            print("Cant milk a male cow! LOL!")
        if namey == "cow2":
            if cow2.energy <= 0
            cow2.cattle_milk()
        if namey == "cow3":
            cow3.cattle_milk()
    else:
        print("Invalid input!")
    

    

        




################################################################################################
# class Animal(object):
#     def __init__(self, animal_type, age, gender, size, color):
#         self.animal_type = animal_type
#         self.age = age
#         self.gender = gender
#         self.size = size
#         self.color = color
    
#     def greeting(self):
#         print(f"Hi! I am a talking animal of type {self.animal_type}")

# simba = Animal("mammal", 4, "male", "large", "brown")

# simba.greeting()

# class Dog(Animal):
#     def __init__(self, animal_type, age, gender, size, color, name, breed):
#         # initing child class will give it new arguments and the parent arguments wont exist.
#         # If only parent class arguments are required, skip __init__
#         # If additional arguments are required, use super()
#         # super will call the __init__ of parent first then add arguments
#         super(Dog, self).__init__(animal_type, age, gender, size, color)
#         self.name = name
#         self.breed = breed

# jacky = Dog("mammal", 6, "male", "medium", "black", "jacky", "golden retriever")

# jacky.greeting()

# print(type(jacky))
# print(type(simba))

# class petDog(Dog):
#     def __init__(self, animal_type, age, gender, size, color, name, breed, owner, toy, city):
#         super(petDog, self).__init__(animal_type, age, gender, size, color, name, breed)
#         self.owner = owner
#         self.toy = toy
#         self.city = city
#         self.energy = 0

#     def play(self):
#         if self.energy > 0:
#             self.energy -= 1
#             print(self.energy)
#         else:
#             print("No energy!")

#     def feed(self):
#         if self.energy > 10:
#             print("OVERFEEDING!")
#         else:
#             self.energy += 5
#             print(self.energy)


# goofy = petDog("mammal", 8, "female", "large", "grey", "goofy", "greyhound", "Karan", "Ball", "Bengaluru")
# goofy.greeting()
# print(type(goofy))

# while True:
#     action = input("Enter f to feed, p to play: ")
#     if action == "f":
#         goofy.feed()
#     elif action == "p":
#         goofy.play()
#     else:
#         print("Invalid")


######################################################################################################3

# class Dogs(object):
#     def __init__(self, name, breed, age, gender, size, color):
#         self.name = name        
#         self.breed = breed
#         self.age = age
#         self.gender = gender
#         self.size = size
#         self.color = color
    
#     def greeting(self):
#         print("Welcome to the DOG SHOW 2019!!")
#         print("Details")
#         print(f"Name: {self.name}")
#         print(f"Breed: {self.breed}")
#         print(f"Gender: {self.gender}")
#         print(f"Size: {self.size}")
#         print(f"Color: {self.color}")

# simba = Dogs("Simba", "German Shephard", 4, "male", "large", "black")
# michelangelo = Dogs("Michael Angelo", "Golden Retriever", 2, "male", "large", "brown")
# athena = Dogs("Athena", "Pomeranian", 3, "female", "medium", "black")
# pewpew = Dogs("Simba", "Chihuahua", 1, "female", "small", "grey")

# simba.greeting()
