# Handling any arguments
def decorator(func):
  def wrapper(*args, **kwargs):  # *args accepts positional arguments
    result =func(*args, **kwargs)  # **kwargs accepts keyword arguments
    return result                 # kwargs is a dictionary of keyword arguments
  return wrapper

# 'variable = decorator(add)' is the same as using @decorator
@decorator  # Calls the decorator with the add function
def add(a,b):
  return a + b

add(10,20)


'''Timing decorator example'''

import time # Import time module
from functools import wraps  # Import wraps from functools

# Decorator function
def show_time(function):
    # Preserves the original function information
    @wraps(function)    # Keeps the original function metadata

    def wrapper(*args, **kwargs):
        start = time.time()                                 # Store the starting time
        result = function(*args, **kwargs)                  # Run the original function
        print(f"Time taken: {time.time() - start:.4f}s")    # Print execution time
        return result
    return wrapper


@show_time
def train_one_epoch():
    time.sleep(2)
    print("Training completed!")
train_one_epoch()


# Context Manager

# Manual file handling
file = open('/content/sample_data/mnist_test.csv') # Open the file
content = file.read()                   # Read the file content
print(content)                          # Print the content
file.close()                            # Close the file


# File handling using context manager
with open('/content/sample_data/mnist_test.csv') as file: # Open the file safely
    content = file.read()

print(content) # Print the file content


# __enter__ and __exit__

class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_value, tb):
        print("Leaving")
with MyContext():
    print("Inside")


# Worked Example

import time # Import time module
from contextlib import contextmanager # Import contextmanager

@contextmanager # Create a context manager
def timer():
    start = time.time() # Store the starting time
    try:
        yield
    finally:
        print(f"Time: {time.time() - start:.4f}s") # Print execution time
with timer():
    train_one_epoch()