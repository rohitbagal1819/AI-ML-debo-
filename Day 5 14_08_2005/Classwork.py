''' Day 6: Python Fundamentals
   Date : 14 -Aug -2026
   Name: Rohit Sanjay Bagal
   Contact no : 9403780042
   Email : rohitbagal1819@gmail.com
   Description : Topics that are covered on day 6
   Topics : 1) Iterators, 2) Generators, 3) Decorators, 4) Context Manager (self)
   7) Special Methods
'''


for nums in [10,20,30]: # Iterable - from which we can get elements one by one
  print(nums)


# Iterator - an object that gives us elements one by one

nums =[10,20,30]
iterator = iter(nums)
print(next(iterator))
print(next(iterator))


iterator = iter([10,20])  # StopIteration: it throws an error when there are no more elements
print(next(iterator))
print(next(iterator))
print(next(iterator))


class Countdown:  # Create a class
  def __init__(self,start):  # Create the init method
    self.current =start

  def __iter__(self):  # The iter method makes the object iterable
    return self

  def __next__(self):  # The next method returns the next element
    if self.current <0:
      raise StopIteration

    number =self.current
    self.current -= 1
    return number


for number in Countdown(3):
  print(number)


# Assignment - Create an iterator using the iter and next methods.
# Create a list with 3 elements and call the iterator 4 times.
# HW


iterator = iter(['a','b','c']) 
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # StopIteration occurs on the 4th call because there are only 3 elements


def get_num():
  yield 10  # yield is used to return a value from the generator function
  yield 20
  yield 30


get = get_num()
print(next(get))  # We are explicitly getting the next value from the generator
print(next(get))
print(next(get))


# Why do we get different values?
# Because this is a generator and it remembers its current position.


def count_up_to(limit):
  num = 1
  while num <= limit:
    yield num
    num += 1


for num in count_up_to(5):
  print(num)


num =list(
    range(1,1_000_001)   # Buffer: all values are stored in memory
)


def num():
  for n in range(1,1_000_001):   # Like a restaurant: values are generated when needed
    yield n


# List comprehension
[n *n for n in range(5)]


# Generator expression
(n*n for n in range(5)) # Creates a generator by replacing [] with ()


sq =(n*n for n in range(5))

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))


def even_num(limit):
  for num in range(2,limit+1,2):
    yield num


for num in even_num(10):
  print(num)


# Assignment
def even_num():
  for num in range(2,11,2):   # start: 2, stop: 11, step: 2
    yield num


for num in even_num(): # This for loop gets and prints the next number
  print(num)



"""# Decorator"""


def say_hello():                                     # Define a function
    user_name = str(input('Enter Your name:'))
    print(f"hello, {user_name}!!")


# A decorator is a function that takes another function as an argument
def decorator(func):   # Define a decorator to modify another function
    def wrapper():    # Wrapper is the new function that replaces the original function
        print("bol na bhidu")
        func()

    return wrapper


hel = decorator(say_hello)  # Pass the function into the decorator and store the result in hel

hel()


# Syntax: @decorator


def decorator(func):
    def wrapper():
        print("bol na bhidu")
        func()

    return wrapper


@decorator
def say_hello():
    user_name = str(input("Enter Your name:"))
    print(f"hello, {user_name}!!")


say_hello()



# Handling any number of arguments
def decorator(func):
  def wrapper(*args, **kwargs):
    result =func(*args, **kwargs)
    return result

  return wrapper


@decorator
def add(a,b):
  return a + b


add(10,20)