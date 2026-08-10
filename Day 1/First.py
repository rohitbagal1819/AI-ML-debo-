''' Day 1: Python Fundamentals
   Name: Rohit Sanjay Bagal
   Day: Sunday
   Date: 09/08/2026
   Cohort: AI-ML 2026
   Contact no: 9403780042
   Email: rohitbagal1819@gmail.com
   Description: Topics that are covered on day 1
   Topics: 1) virtual environment ,2) vscode/jupyter notebook/kaggle ,3) commands ,4) DataTypes, 5) dictionary, 6) List , 
   7) Indexing, 8) Slicing , 9)Conditional Statements, 10)For loop, 11) While loop'''

# Question 1 - datatype and their type
x = 1.2
print(type(x))

# Question 2 - User input
x = int(input("Enter a valid number: "))
print(x)

# Question 3 - type conversion
a = "12345"
b = int(a)
print(b)

# Question 4 - learn how to use the dictonary
dict = {"x": "shraddha", "y": "rohit", "z": "mayank", "a": "rohit" }
print(dict["x"])

# Question 5 - learn how to use the list items and access them
list = ["rohit", 2.5, 1000, ]
print(list[1])

# Question 6 - learn slicing
a = "Here im learning new Technology"
print(a[2:])
print(a[0 : 6])
print(a[0 : 13])
print(a[: 13])

# Question 7 - learn if - else statements(conditional statements)
a = int(input("enter the age: "))
if(a > 18):
    print("you can drive")
else:
    print("you cannot")

# Question 8 - Advance example of the if - else statement
a = int(input("Enter the total attendance of deboistech: "))
if(a >= 80):
    print("You can get the certificate")
elif(a >= 60):
    print("First complete your attendance")        
else:
    print("you cannot getting a certificate")



# ============================================ HOMEWORK ====================================================

# 1) For loop example and learning

# Example no - 1
for i in range(1, 11):
    print(i)

# Example no - 2
lists = ["ramu", "shamu", "rohu", "gauru", "sakshu"]

for list in lists:
    print(list)

# Example no - 3
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
    
# ==============================================================================

# 1) while loop example and learning

# Example no - 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Example no - 2
# students = ["rohit", "gaurav", "kunal", "vaibhav"]
i = 0
while i < len(students):
    print(students[i])
    i += 1

# ==============================================================================

# String to number conversion

a = "12345"
b = int(a)
print(b)

a = 12345
b = str(a)
print(type(b))

# ==============================================================================

# Tuple - It is immutable, means we cannot change if we declare the tuple.
# it is represent int he parenthesis.

subject = ("java", "python", 99, "dbms", "os")

print(subject[0])
print(subject[2])
print(subject[3])

# ==============================================================================

# List - It is mutable, means we can change the elements in the list.
# it is represented int the square braces

list = ["ramu", "shamu", True, 2.44, 5, "jayshivraj"]

print(list[0])
print(list[1])
print(list[2])
print(type(list[2]))









