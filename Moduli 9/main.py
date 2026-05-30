'''
class Animal :
    def sound(self):
        print("some generic animal sound")
class Dog(Animal):
    def sound(self):
        print('wooff')

class cat(Animal):
    def sound(self):
        print("meow")


animal=Animal()
animal.sound()

pitbull=Dog()
pitbull.sound()

british=cat()
british.sound()
'''


'''
class vertebrate:
    def __init__(self,backbone=True):
        self.has_backbone=backbone

    def vertebrate_info(Self):
        print("Vertebrates have a backbone")


class Aquatic:
    def __init__(self,habitat="water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatic animals live in water")


class Fish(vertebrate,Aquatic):
    def __init__(self,species,backbone=True,habitat="Water"):
        super().__init__(backbone=backbone)
        self.habitat =habitat
        self.species = species

def fish_info(self):
    print|(f'The {self.species} is a type of fish found in {self.habitat}')

def swim (self):
    print("the fish is swiming")

goldfish=Fish("goldfish")
print(goldfish.has_backbone)
print(goldfish.habitat)
'''















class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f'The students name is {self.name} and he has a {self.grade} ')


class PrimaryStudent(Student):

    def study(self):
        print("He is in primary school")

class HighSchool(Student):

    def study(self):
        print("He's in highschool")


Olti=Student('olti',17)
Olti.introduce()


dion=PrimaryStudent("dion",13)
dion.study()

leart=PrimaryStudent("leart",13)
leart.study()


Ensar=HighSchool("Ensar",18)
Ensar.study()

Haris=HighSchool("Haris",18)
Haris.study()













'''
class dog:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def sound(self):
        print(f'{self.name} makes the sound woof and is {self.age}')


class cat :
    def __init__(self,age,name):
        self.age = age
        self.name =name

    def sound(self):
        print(f'{self.name} makes the sound meow and is {self.age}')


pitbull=dog("Buddy",12)
pitbull.sound()

british = cat ("christina",10)
british.sound()
'''