# Day 5 — Bank Account Management System

## Project Description

This is a simple Python project based on **Object-Oriented Programming (OOP)**.

In this project, we create a `BankAccount` class that represents a bank account.

The program allows us to:

- Create a bank account
- Store the account owner's name
- Store the account balance
- Deposit money
- Withdraw money
- Check the available balance
- Handle insufficient balance

---

## Program Code

```python
# ---------------- Bank Account Example ----------------

# Creating a class for the bank account.
# This class works as a blueprint for creating bank accounts.
class BankAccount:

    # __init__() is the constructor.
    # It runs automatically when an object is created.
    def __init__(self, owner, balance):

        # Store the owner's name inside the object.
        self.owner = owner

        # Store the starting balance inside the object.
        self.balance = balance

    # This method is used to deposit money.
    def deposit(self, amount):

        # Add the deposit amount to the current balance.
        self.balance += amount

    # This method is used to withdraw money.
    def withdraw(self, amount):

        # Check whether enough balance is available.
        if amount <= self.balance:

            # Subtract the withdrawal amount.
            self.balance -= amount

        else:

            # If balance is not enough, display a message.
            print("Insufficient balance")

    # This method displays the current balance.
    def show_balance(self):

        # Print the current balance.
        print(f"Balance: {self.balance}")


# Creating a BankAccount object.
# Owner = Gaurav
# Initial balance = 5000
acc = BankAccount("Gaurav", 5000)


# Deposit ₹1500 into the account.
acc.deposit(1500)


# Withdraw ₹2000 from the account.
acc.withdraw(2000)


# Display the final balance.
acc.show_balance()
```

---

## Output

```
Balance: 4500
```

# Program flow

```
BankAccount Program
│
├── 1. Define class BankAccount
│       └── (blueprint only, nothing executes yet)
│
├── 2. Create object: acc = BankAccount("Gaurav", 5000)
│       └── __init__() runs
│              ├── self.owner = "Gaurav"
│              └── self.balance = 5000
│
├── 3. acc.deposit(1500)
│       └── self.balance += amount
│              └── 5000 + 1500 = 6500
│
├── 4. acc.withdraw(2000)
│       └── if amount <= self.balance
│              ├── True (2000 <= 6500)
│              │      └── self.balance -= amount
│              │             └── 6500 - 2000 = 4500
│              └── False
│                     └── print("Insufficient balance")
│
└── 5. acc.show_balance()
        └── print(f"Balance: {self.balance}")
               └── Output: "Balance: 4500"
```