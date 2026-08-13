''' Day 5: Advance Python
   Date : 13 -Aug -2026
   Name: Rohit Sanjay Bagal
   Contact no : 9403780042
   Email : rohitbagal1819@gmail.com
   Description : Topics that are covered on day 5
   Topics : 
        1. Defining and Calling Functions
        2. Function Parameters and Return Values
        3. Python Type Hints
        4. Type Hints for Variables
        5. Type Hints with Collections
        6. Union Type Hints (`int | str`)
        7. Classes and Objects
        8. `__init__()` Constructor and Methods
        9. `__str__()` and `__repr__()`
        10. Multiple Objects and Instance Variables'''

# Adding two values using a function
def add(a, b):
    return a + b
add(2, 5)

# Here int is only a hint.
def add(a: int, b: int):
    return a + b
add("ram", "sham")


# We can also give a type hint while creating a variable.
name: str = "Sakshi"
age: int = 20
height: float = 5.4
is_student: bool = True
print(name)
print(age)
print(height)
print(is_student)

# Basic syntax:
# variable_name: type = value


# The function expects a number and also says that
# the returned value should be an integer.
def square(number: int) -> int:
    return number * number


# This function doesn't take anything,

def get_name() -> str:
    return "Zutopia"
square(2)
get_name()


# If a value can be either int or str
def print_id(user_id: int | str):
    print(user_id)
print_id(101)
print_id("qwerty")


# Type hints can also be used with collections.
numbers: list[int] = [10, 20, 30]
student_marks: dict[str, int] = {"Alice": 90}
point: tuple[int, int] = (10, 20)
print(numbers)
print(student_marks)
print(point)


# Function for printing string double times
def double(number: int) -> int:
    return number * 2
double("Hi")


# Type hints are mainly useful for understanding the code,
# documentation and tools like VS Code.
# They don't automatically force the type at runtime.


# Here marks should be a list containing integers.
def calculte_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)

def display_student(name: str, marks: list[int]) -> None:
    average: float = calculte_average(marks)

    print(f"Student: {name}")
    print(f"Average: {average:2f}")
display_student("Sakshi", [85, 90, 94])

# ---------------- Classes and Objects ----------------

# Creating a very simple class.
# pass means we are not putting anything inside it yet.
class Students:
    pass
s1 = Students()
s2 = Students()

s1.name: str = "Sakshi"
s1.marks: list[float] = [23, 63, 98]
print(s1.name)
print(s1.marks)


# __init__ runs automatically whenever we create an object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Sakshi", 20)
print(name)
print(age)


# We can create multiple objects from the same class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Sakshi", 20)
student2 = Student("Shraddha", 21)
print(student1.name)
print(student2.name)


# A class can contain both data and functions.
# The function inside a class is called a method.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and {self.age}")
student1 = Student("Rohit", 20)
student2 = Student("Gaurya", 50)
student1.introduce()
student2.introduce()

# ==============================================================================

# ---------------- Bank Account Example ----------------

# This is a practical example of a class.
# Each bank account object will have an owner and balance.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Adding money to the account.
    def deposit(self, amount) -> float:
        self.balance += amount

    # Taking money out only if there is enough balance.
    def withdraw(self, amount) -> float:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    # Just displaying the current balance.
    def show_balance(self) -> float:
        print(f"Balance: {self.balance}")


# Creating a bank account with an initial balance of 5000.
account = BankAccount("Sakshi", 5000)

account.deposit(1500)       
account.withdraw(2000)     
account.show_balance()      

# ==============================================================================

# ---------------- __str__ and __repr__ ----------------

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name!r}"
student = Student(20)
print(student)
print(repr(student))

# This is another __repr__ function written separately.
# It does NOT change the Student class because it is outside the class.
def __repr__(self):
    return f"{self.name!r}"
print(repr(student))

