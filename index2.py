# Base Class
class Animal:
    def move(self):
        return "This animal moves in some way."

# Derived Classes
class Bird(Animal):
    def move(self):
        return "Flying in the sky! 🕊️"

class Fish(Animal):
    def move(self):
        return "Swimming in the water! 🐟"

class Dog(Animal):
    def move(self):
        return "Running on land! 🐕"

# Demonstration of Polymorphism
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    print(animal.move())
