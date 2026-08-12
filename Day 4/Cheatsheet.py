# Numbers
# Arithmetic
a = 20
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Modulus
a = 17
b = 5
print(a % b)
print(a // b)

# Power
a = 2
b = 4
print(a ** b)

# Average
a = 80
b = 90
c = 70
avg = (a + b + c) / 3
print(avg)

# Precedence
a = 10
b = 5
c = 2
result = a + b * c
print(result)

# ============================================
# String
# Index
name = "Rohit"
print(name[0])
print(name[2])
print(name[-1])

# Slice
name = "Python"
print(name[0:3])
print(name[:4])
print(name[2:])

# Methods
name = "rohit"
print(name.upper())
print(name.lower())
print(name.replace("rohit", "rahul"))

# Operations
a = "Hello"
b = "Python"
print(a + " " + b)
print(a * 3)
print("Python" in b)

# Format
name = "Rohit"
age = 21
print(f"My name is {name}")
print(f"My age is {age}")

# ==============================================
# List
# Index
nums = [10, 20, 30, 40]
print(nums[0])
print(nums[-1])
nums[1] = 50
print(nums)


# Add
nums = [10, 20, 30]
nums.append(40)
nums.insert(1, 15)
print(nums)

# Remove
nums = [10, 20, 30, 40]
nums.remove(20)
print(nums)
x = nums.pop()
print(x)
print(nums)

# Sort
nums = [50, 10, 40, 20, 30]
nums.sort()
print(nums)
nums.reverse()
print(nums)

# Loop
names = ["Rohit", "Rahul", "Amit"]
for i, name in enumerate(names):
    print(i, name)

# ==============================================
# Tuple
# Index
data = ("Rohit", 21, "Java")
print(data[0])
print(data[1])
print(data[-1])

# Slice
nums = (10, 20, 30, 40, 50)
print(nums[1:4])
print(nums[:3])
print(nums[2:])

# Unpack
data = ("Rohit", 21, "Java")
name, age, course = data
print(name)
print(age)
print(course)


# Methods
nums = (10, 20, 20, 30, 20)
print(nums.count(20))
print(nums.index(30))

# Convert
nums = [10, 20, 30]
data = tuple(nums)
print(data)
nums = list(data)
print(nums)

# ==============================================
# Dictionary
# Access
student = {
    "name": "Rohit",
    "age": 21,
    "marks": 85
}
print(student["name"])
print(student["marks"])

# Add
student = {
    "name": "Rohit",
    "age": 21
}
student["course"] = "Java"
print(student)

# Update
student = {
    "name": "Rohit",
    "age": 21
}
student["age"] = 22
print(student)

# Get
student = {
    "name": "Rohit",
    "age": 21
}
print(student.get("name"))
print(student.get("marks", "Not found"))

# Loop
student = {
    "name": "Rohit",
    "age": 21,
    "course": "Java"
}
for key, value in student.items():
    print(key, value)

# ==============================================
# Set
# Duplicate
nums = {10, 20, 10, 30, 20}
print(nums)

# Add
nums = {10, 20, 30}
nums.add(40)
print(nums)
nums.remove(20)
print(nums)

# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# Difference
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)
