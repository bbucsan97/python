


#num1 = 2+3j
#num2 = complex(2,3)
#in case of an imaginary number use variable.imag
#print(num2.real, num2.imag)

#from enum import Enum

#class State(Enum):
 #   INACTIVE = 0 
  #  ACTIVE = 1

#print(State.ACTIVE.value)


#print("What is your age")
#age = input()
#print("Your age is " + age)


#dogs = ["Roger", 1, "Syd", True, "Quincy", 7]
#replaces syd with beau [2] within a list can use negative number to go from front to back
#dogs[2] = "Beau"

#adds item to list
#dogs.append("Judah")
#adds item to list remember square brackets
#dogs.extend(["Judah" , 5])
#add items to list
#dogs += ["Judah", 5]

#remove item
#dogs.remove("Quincy")
#remove and return single item


#print(dogs)

#items = ["Roger", "bob", "Syd", "tom", "Quincy", "lol"]

#items.insert(2, "Test")

#items[1:1] =["Test1"]


## has to be  the same type in the list or it will error out
#items.sort() 
#itemscopy = items[:]
#if you want to not care about lower case and upper case use :
#items.sort(key=str.lower)
#print(items)
#print(itemscopy)

#items = ["Roger", "bob", "Beau", "Quincy"]
#sorts without modifying original list
#print(sorted(items,key=str.lower))

#print(items)

#TUPLES: immutable objects, once created they cannot be modified

#names = ("Roger", "Syd")

#names[0]
#names.index("Roger")

#len(names)

#print("Roger" in names)
#print(sorted(names))

#you can combine two tuples but never modify a tuple and add to it.
#newTuple = names + ("Tina", "Quincy")
#print(newTuple)

#dictionaries
# can be ANY value pair as follows below
#dog = { "name": "Roger", "age": 8, "color": "green "}

#dog["name"] = "Syd"

#print dictionary as a list
#print(list(dog.items()))
#print(len(dog))

#delete key value pair 
#del dog['color']

#print(dog)

# Sets

#set1 = {"Roger", "Syd"}
#set2 ={'Roger'}
#prints the intersection with intersect
#intersect = set1 & set2
#print(intersect)
#print(list(set1)) - makes set into a list
#SETS CANNOT HAVE TWO OF THE SAME ITEM

#Functions
#arguments are values passed to the function. Can have default value if not specified 
#parameters the values accepted by the function inside the function definition
#parameters are past by references
#def hello(name):
 #   if not name:
  #      return name, "Beau", 8
#hello(False)

#nested functions
# function.split will print it on new line
#def talk(phrase):
 #   def say(word):
  #      print(word)

   # words = phrase.split(' ')
    #for word in words:
     #   say(word)
#talk("I am going to buy the milk")

## nonlocal *variable *:  will allow you to access the variable that was declared from an outer fucntion

#def count():
 #   count = 0

  #  def increment():
   #     nonlocal count
    #   return count

    #return increment

#increment = counter()


#objects

#age = 8

#print(age.real)
#print(age.imag)
#print(age.bit_length)

#items = [1, 2]
#items.append(3)
#items.pop() #remove and return last time which is 3 in this case
#print(id(items))

#age = 8 

#age = age + 1

#Loops

#condition = True
#while condition == True:
  #  print("The condition is True")
 #   condition = False

#count = 0
#while count < 10:
 #   print("The condition is True")
  #  count = count + 1

#print("After the loop")

#for loops - iterate items in a list ;;breaks the loop entirely if use break 
# continue is used to skip code in a loop
#items = [1, 2, 3, 4 ]
#for item in items:
 #   if item == 2:
  #      continue
   # print(item)

#iterate in a range
#for item in range(15):
 #   print(item)

# for index
#items = [1, 2, 3, 4 ]
#for index, item in enumerate(items):
 #   print(index, item)

#classes 
#object is an instance of a class
#SELF is to be used when creating class ALWAYS
## Classes can inheirt from other classes
#class Animal:
  #  def walk(self):
 #       print("Walking...")

#class Dog(Animal):
    #def __init__(self, name, age):
    #    self.name = name
   #     self.age = age

  #  def bark(self):
 #       print("woof!")
#
#roger = Dog("Roger", 8)
#print(roger.name)
#print(roger.age)
#roger.bark()
#roger.walk()

#Modules can import functions and other things from other files by using:
# import (filename wihout the extension) or you can do as below
#from dog import bark
#__init__.py lets python know it is a folder that ]
#from lib.dog import bark
# these are custom ones that you can create and work with

#import math - math utilities
#import re - regular expressions
#import json work with JSON
#import datetime
import sqlite 3