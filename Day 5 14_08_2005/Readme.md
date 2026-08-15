# Decorators and Context Managers in Python

## 1. Decorators

A decorator adds extra functionality to a function without changing its code.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    return a + b
```

- `*args` → positional arguments, stored as a tuple
- `**kwargs` → keyword arguments, stored as a dict

---

## 2. Timing Decorator

```python
import time
from functools import wraps

def show_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.4f}s")
        return result
    return wrapper

@show_time
def train_one_epoch():
    time.sleep(2)
```

---

## 3. `@wraps`

Preserves the original function's `__name__` and docstring so the wrapper doesn't hide them.

```python
from functools import wraps

@wraps(func)
def wrapper(*args, **kwargs):
    ...
```

---

## 4. Context Managers

Used when something needs to be opened and properly closed (e.g. files).

```python
with open('data.csv') as file:
    content = file.read()
```

The `with` statement automatically closes the file — no manual `file.close()` needed.

---

## 5. `__enter__()` and `__exit__()`

A context manager can be built using these two special methods.

```python
class MyContext:
    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, *args):
        print("Leaving")

with MyContext():
    print("Inside")
```

**Output:**
```
Entering
Inside
Leaving
```

---

## 6. `@contextmanager`

A shorter way to write a context manager.

```python
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Time: {time.time() - start:.4f}s")

with timer():
    train_one_epoch()
```

> Use `try/finally` around the `yield` if the wrapped code might raise an exception.

---

## Summary

- How decorators work, and how `@decorator` works internally
- Difference between `*args` and `**kwargs`
- Measuring execution time with a decorator
- Why `@wraps()` is used
- What context managers are and how `with` works
- How `__enter__()` / `__exit__()` work
- How `@contextmanager` simplifies context manager creation