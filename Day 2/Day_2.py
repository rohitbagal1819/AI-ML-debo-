# Arithmetic operators

a = int(input("enter the number: "))
b = int(input("enter the number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Power operator
a = 2 ** 5
print(a)


# modulo
a = 10 % 5
print(a)


# integer division
a = 22 // 8
print(a)


# Concatanation
a = "10"
b = "5"
print(a + b)


# Concatanation of the string
a = "rohit"
b = "bagal"
c = " "
print(a + c + b)


# Replication of the code
a = "hi " * 4
print(a)


# let's change the value
var1 = 3.14
print(var1)

var1 = "alice"
print(var1)


# Naming convension
# There are three type of cases
# 1. snake case 2. camel case 3. pascal case (personal understanding)

# Snake case
my_name = "rohit"
print(my_name)

# Camel case
myName = "Rohit Bagal"
print(myName)

# Pascal case
MyName = "Rohit_Bagal"
print(MyName)


# Length function

a = len("rohit")
print(a)


# Type Conversion
print("This is", str(5), "word sentence")
print("The age of baby is:", float(3))
print("The num is an integer:", int(5.33))


# Round function
a = round(5.6)
print(a)
b = round(5.124355)
print(b)

# Absolute function(basically it is mod of the math).
a = abs(-100)
print(a)

# Comparison (relational) operators
a = 10
b = 10
if a == b:
    print("Equal")
else:
    print("Not equal")


if a != b:
    print("not equal: ")
elif a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
elif a <= b:
    print("a is less than or equal to b")
elif a >= b:
    print("a is greater than or equal to b")
else:
    print("i dont know")


# And or not
username = str(input("Enter username: "))
password = str(input("Enter password: "))

if username == "admin" and password == "pass":
    print("password is correct")
else:
    print("not correct")
    
# Not
print(not(True))

# Or
a = 10
b = 20

if a > 15 or b > 15:
    print("At least one condition is true")
else:
    print("Both conditions are false")
