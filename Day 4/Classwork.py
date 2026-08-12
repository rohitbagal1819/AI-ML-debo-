''' Day 4: Python Fundamentals
   Date : 12 -Aug -2026
   Name: Rohit Sanjay Bagal
   Contact no : 9403780042
   Email : rohitbagal1819@gmail.com
   Description : Topics that are covered on day 4
   Topics : 1) Defining Function, 2) calling function ,3) None ,4)  Local scope , 5) Global scope , 
   7)Exception handling, 8) Minor project'''

# Creating a function
# A reusable block of code, written once and run as many time as you like

# def is a keyword to make or create a function
def hello():
  print("hey")
  print("hey")
  print("hey")
hello()
hello()
print("One more time")
hello()


# Sum of two numbers
def sum(a, b): # parameters
    return a + b # return statement

a = int(input("Enter the first num: "))
b = int(input("Enter the second num: "))

print(sum(a, b))


# All types of Division's
def All_Dividion(a, b):
  division = a / b
  integer_division = a // b
  modulo = a % b

  print(division," | ", integer_division," | ", modulo)
All_Dividion(22, 8)


# add
def add(a, b):
  return a + b

result = add(4, 5)
print(result)


# getting a random number
import random
def get_answer(n):
  if n == 1:
    return "It is certain"
  elif n == 2:
    return "Ask again later"

r = random.randint(1, 9)
print(get_answer(r))


# How to use "Node" and where we have to use
spam = None
print(spam)


# Local scope
def spam():
  eggs = "hi"
  print(eggs)

# Code in the global scope can't use any local variable
# A local scope cant use variable from another function's local scope
# Code in a local scope can read global variable
# The same name can be reused in different scope they are different variabel


# Both global and local scope had a same name
eggs = "global"
def spam(): # creating a function
  eggs = "local" # local variable
  print(eggs) # local print
spam() # function calling

print(eggs) # global print

"""Try / except - the mechanism

Def :- When the exception is occur's a program will be terminate. 
    So we use an mechanism to stop this is called try / except that
     insures that if code is containing a particular error then goes
      beyoud that particular line where the error is occuring.
"""

# Cannot divide by zero exception
42/0


# Working function that executing an code that containing error
def divide_by(n):
  return 42 / n

print(divide_by(2))
print(divide_by(12))
print(divide_by(0))
print(divide_by(6))


# Correct code that show how actually a try / except works
def spam(divide_by):
  try:
    return 42 / divide_by
  except ZeroDivisionError:
    print("Error: Invalid arguments")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(3))

# ZeroDivisionError - Divide by zero
# ValueError        - Right type, wrong value
# TypeError         - Mismatched type
# IndexError        - List index out of range

#========================================= HOMEWORK====================================


# 1. ZeroDivisionError
def ZDE():
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero.")
ZDE()      

# 2. ValueError
def VE():
  try:
      number = int("hello")
  except ValueError:
      print("invalid value conversion.")
VE()

# 3. TypeError
def TE():
  try:
      total =  "age:"+ 25
  except TypeError:
      print("mismatched data type.")
TE()

# 4. IndexError
def IE():
  try:
      items = [1, 2, 3]
      val = items[5]
  except IndexError:
      print("Index err0r occurs!")
IE()