# Python Interview Questions

## [Top 100 Python Interview Questions You Must Prepare In 2021 - Edureka](https://www.edureka.co/blog/interview-questions/python-interview-questions/)

### Q28 What are the generators in python?

[Link](https://www.programiz.com/python-programming/generator)

There is a lot of work in building an iterator in Python. We have to implement a class with `__iter__()` and `__next__()` method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a `yield` statement instead of a `return` statement.

### Q32 What are docstrings in Python?

Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well. Often used to add some documentation about a class or function.

```python

def sum(x, y):
    """
    Function to return the sum of 2 numbers.
    :type x: int
    :type x: int
    :rtype: int
    """
    return x + y
```

### Q34 What is the usage of help() and dir() functions in Python?

Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions.

Help() function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.

Dir() function: The dir() function is used to display the defined symbols.

```python

import os
help(os)
dir(os)
```

### Q37 How can the ternary operators be used in python?

```python
x = True if 5==5 else False
```

### Q38 What does this mean: `*args`, `**kwargs`? And why would we use it?

We use `*args` when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. `**kwargs` is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use `*bob` and `**billy` but that would not be wise.

### Q50. How is Multi-threading achieved in Python?

- [Processes and Threads - Microsoft](https://docs.microsoft.com/windows/win32/procthread/processes-and-threads)
- [Thread - Tech With Tim](https://youtu.be/olYdb0DdGtM)
- [Example Code](src/thread.py)

```python

# thread.py

import threading
import time


def feed_dog(food):
    print('Begin feeding the dog.')
    print(f"The dog is eating {food}.")
    time.sleep(5)
    print('Feeding the dog complete.')


def feed_cat(food):
    print('Begin feeding the cat.')
    print(f"The cat is eating {food}.")
    time.sleep(5)
    print('Feeding the cat complete.')


x = threading.Thread(target=feed_dog, args=("food",))
x.start()

y = threading.Thread(target=feed_cat, args=("food",))
y.start()

print(f"Total threads = {threading.activeCount()}")
```
