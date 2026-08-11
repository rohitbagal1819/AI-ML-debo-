''' Day 3: Python Fundamentals
   Name: Rohit Sanjay Bagal
   Day: Tuesday
   Date: 11/08/2026
   Cohort: AI-ML 2026
   Contact no: 9403780042
   Email: rohitbagal1819@gmail.com
   Description: Today is the day where i learn the midium level of python fundamentals....
   Topics:
      1. While Loop
      2. Break and Continue Statements
      3. For Loop
      4. range() Function
      5. Loop Control Statements
      6. User Input and Loops
      7. Python Modules
      8. random Module
      9. sys Module
      10. os Module
      11. math Module
      12. Importing Functions from Modules
      13. sys.exit() Function
      14. Module Naming Conflicts
      15. Project'''


# Wrong if code
spam = 0
if spam < 5:
  print("hello world")
  spam = spam + 1


  # Correct while loop code
spam = 0
while spam < 5:
  print("hello world")
  spam = spam + 1


  # A real use of the while loop
name = ""
while name != "Rohit":
  print("please type your name: ")
  name = input("")
print("Thank you")  


# Use of the break statement
while True:
  print("Type your name: ")
  name = input("")
  if name == "Rohit":
    break
print("Thank you!")    


# Continue statement
for num in range(10):
  if num % 2 == 0:
    continue
  print(num)


# If the break statement is executing in the in the block of code then it will terminate the program.
# In the continue statement it will not execute the current true statement.


# For loop (stop)
for i in range(5):
  print("Hello!")


# For loop one parameter(start)
for i in range(5):
  print(i)


# For loop two parameter(start, stop)
for i in range(2, 6):
  print(i)  


# For loop three parameter(start, stop, step)
for i in range(0, 11, 2):
  print(i)  


# Adding up 0 through 100
total = 0
for i in range(101):
  total = total + i
print(total)    


# import random number
import random
print(random.randint(1, 10))


# Sys - it can communicate with the environment of the system.
# Ramdom - it gives us a random number.
# OS - operating system interface: connect with the files, directory.
# Math - Mathematical function are alreasy in the module like power, trignometric, algebraic and many more.

# Python finds your random.py before rhe real module - and every random. call now break.


# module import
from random import *
print(randint(1, 100))


# Type exit to quit
import sys

while True:
  print("Type to exit: ")
  response = input("")
  if response == "exit":
    sys.exit()
  print("You typed" + response)  

