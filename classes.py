# Object oriented programming concepts

# classes - blueprint
# Objects - is the instance of the class

# Creating classes

class Dog():
    #state
    # constructor - default functions to be execute when you create an object 
    def __init__(self, breed, color, name):
        self.breed = breed
        self.color = color
        self.name = name


    def describeDog(self):
        return f"your dog is {self.breed}."

    def run(self):
        return f"Your dog {self.name} is running..."

    def bark(self):
        return f"{self.name} is barking Wouf wouf wouf!!!!"

# instantiating the clas - creating object of the class
rex = Dog('german shepherd', 'brown','Rex')
sharik = Dog('husky','black','Sharik')


#access the class state and behavior 

print(f"the breed of the rex is {rex.breed}")
print(f"the color of the rex is {rex.color}")
print(rex.describeDog())
print(rex.bark())
print(rex.run())

print("================================================")


print(f"the breed of the rex is {rex.breed}")
print(f"the color of the rex is {rex.color}")
print(sharik.describeDog())
print(sharik.bark())
print(sharik.run())



class Car():

    year = 2020

    def __init__(self, color):
        self.color = color

    def car_description(self):
        print(f"describing the car: \ncolor: {self.color}\nyear:{self.year}")


bmw = Car('black')        
lexus = Car('White')



print(bmw.car_description())
print(lexus.car_description())



