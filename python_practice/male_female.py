# 2. Define a class Person and its two child classes: Male and Female. All classes have a method "get_gender" which can print "Male" for Male class and "Female" for Female Class.

# Bonus: Make class Person an abstract class and make get_gender an abstract method in thesame class. The two child classes must inherit and implement get_gender. i.e., When trying to initialize an object of class Person, the program must throw an error.

from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @abstractclassmethod
    def get_gender(self):
        pass

class Male(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_gender(self):
       return 'male'
   

class Female(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_gender(self):
       return 'Female'
   

# The below line will give error since its abstract class
# person_instance = Person() 

male_instance = Male('himanshu',21)
female_instance = Female('ayesha',40)


print(f"{male_instance.name} is {male_instance.age} years old and gender is {male_instance.get_gender()}")


print(f"{female_instance.name} is {female_instance.age} years old and gender is {female_instance.get_gender()}")




        
