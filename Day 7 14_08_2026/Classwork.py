''' Day 7: Python Libraries
   Date : 16 -Aug -2026
   Name: Rohit Sanjay Bagal
   Contact no : 9403780042
   Email : rohitbagal1819@gmail.com
   Description : Topics that are covered on day 7
   Topics : 1. Python Libraries
            2. Math Module
            3. PIP Installation
            4. NumPy
            5. NumPy Arrays
            6. Array Operations
            7. NumPy Built-in Functions
            8. 2D Arrays
            9. Statistical Operations
            10. HTTP Requests & APIs
'''

# This method is used to find the square root of any nymber
# Math is an inbuild python library
import math
math.sqrt(25)

"""1. Math and libraries
2. Files
3. Website and the internet
4. Dates and times
5. Data processing
6. Graph and chart
7. Databases
8. Machine learing models

"""

# Math module - it is workedon an individual module
!pip install numpy

# List is use to store multiple types of data but it is hectic to use to storing and organizing the strucutre data
import numpy as np
numbers = [10, 20, 30]

# The array can onlu store an single type of an element, it is easy to traverse.
import numpy as np
numbers = np.array([10, 20, 30])
print(numbers)

# This is the method where we are using the traditional method to add a number in an array
# It means it traverse the array first and then add(method that we passes) the element which we want
num = [10, 20, 30]
result = []
for n in num:
  result.append(n * 2)
result

# output : [20, 40, 60]

# In above code there is a traditional method like we hard code and if we have the library like numpy then used it in mordern way.
# We first install the library and then import and then use as we want
numbers = np.array([10, 20, 30])
result = numbers * 2
result

# output : array([20, 40, 60])

# This is the in-built method that returns a zero in an array format.
# As you see in the result we ger an array.
np.zeros(5)

# output : array([0., 0., 0., 0., 0.])

# This is the in-built method that returns a one's in an array format.
# # As you see in the result we ger an array.
np.ones(5)

# output : array([1., 1., 1., 1., 1.])

# This is the in-built method that range of array that we define in the arrange function
# like a range function it takes an three parameters such as (starting, stoping, iteration)
# As you see in the result we ger an array.
np.arange(0, 10, 2)

# output: array([0, 2, 4, 6, 8])

# In this array we are changing the element at the specific position and we can print the element that we want by traversing.
numbers = np.array([10, 20, 30])
print(numbers[0])

numbers[1] = 99  # Swapping the element at specific index
numbers

# output :  10
#           array([10, 99, 30])

# Mathematical operation that we are performing.
numbers = np.array([10, 20, 30])
print(numbers + 5)
print(numbers * 2)
print(numbers / 10)

# output :
#          [15 25 35]
#          [20 40 60]
#          [1. 2. 3.]

# Mathematical example which multiply and adding two aarray with the help of indexing.
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print(a * b)

# output :
#         [11 22 33]
#         [10 40 90]

# Functions which calculating sum, mean and maz.
numbers = np.array([10, 20, 30, 40, 50])
print(np.sum(numbers))

print(np.mean(numbers))

print(np.max(numbers))

# output:
#         150
#         30.0
#         50

# This is 2D matrix which give's us the calculation of (row, col)
num = np.array([[1, 2, 3],
               [4, 5, 6]])
print(num.shape)

print(num[0,1])

# output :
#         (2, 3)
#         5

# This library is in-built library which works for request and response for the client server model.
import urllib.request
response = urllib.request.urlopen("https://google.com")
response.status

# output : 200

# GET - it is take data from server.
# and then we get a response as a status code ass 200(ok)
import requests as req
req.get("https://google.com")

res = req.get("https://google.com")
res.status_code

# output : 200

#
import requests as req
res = req.get("https://google.com")
data = res.json()
data["Rohit"]

# We are using the Numpy library and their.
marks = np.array([89, 36, 99, 65])

print("Marks : ", marks)
print("Total : ", np.sum(marks))
print("Average : ", np.mean(marks))
print("Highest : ", np.max(marks))

# output :
#           Marks :  [89 36 99 65]
#           Total :  289
#           Average :  72.25
#           Highest :  99

# We are getting a response from the google like to get and the status code that it is working or not
response = req.get("https://google.com")
response.status_code

# output : 200

# This code provides an error bcz google returns HTML page and we are trying to send data in json
response = req.get("https://google.com")
data = response.json()
data["Rohit"]

# output : 'Rohit'

requests.get("https://google.com")

# syntax of get request
requests.get(url)

requests.get('https://www.google.com/')

# syntax of post request
requests.post(url, json =data)

requests.post('https://www.google.com/', json = {'text':'hello'})