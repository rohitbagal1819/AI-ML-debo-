# 1) Random
# import random

print(random.randint(1, 10))

print(random.random())

print(random.uniform(1, 10))

print(random.randrange(0, 10, 2))

print(random.choice(['1','2','3']))

print(random.choices([1,2,3], k=3))

print(random.seed(42))

print(random.gauss(0, 1))


# ==============================================================================

# 2) Sys
# import sys

print("Hello world!")
sys.exit(0)

print(sys.version)

print(sys.version_info)

print(sys.modules)

print(sys.stdin)

print(sys.maxsize)

print(sys.getrecursionlimit())

print(sys.exc_info())


# ==============================================================================

# 3) OS
# import os

print("Hello world!")

print(os.getcwd())

print(os.listdir("."))

os.mkdir("test_folder")

os.makedirs("parent_folder/child_folder")

os.rename("test_folder", "renamed_folder")

print(os.path.join("folder", "example.txt"))

print(os.path.exists("Day 1"))

print(os.path.isdir("Day 1"))

print(os.path.abspath("Day 1"))

print(os.path.basename("Day 1"))


# ==============================================================================

# 4) Math
import math

print("Hello world!")

# CONSTANT

print(math.pi)

print(math.e)

print(math.tau)

print(math.inf)

print(math.nan)

# -------------------------

# POWER, LOGS AND SQRT

x = 2
y = 4

n = 144
e = 2

print(math.sqrt(x))

print(math.pow(x, y))

print(math.exp(x))

print(math.log2(x))

print(math.isqrt(n))

# -------------------------

# Rounding & rendering

x = 10.638

y = 1.45

print(math.ceil(x))

print(math.floor(x))

print(math.trunc(x))

print(math.fabs(x))

print(math.copysign(x, y))

print(math.fmod(x, y))




