# Python Interview Questions

## [Top 100 Python Interview Questions You Must Prepare In 2021 - Edureka](https://www.edureka.co/blog/interview-questions/python-interview-questions/)

### Q28 What are the generators in python?

[Link](https://www.programiz.com/python-programming/generator)

There is a lot of work in building an iterator in Python. We have to implement a class with `__iter__()` and `__next__()` method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a `yield` statement instead of a `return` statement.

### Q32. What are docstrings in Python?

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

### Q34. What is the usage of help() and dir() functions in Python?

Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions.

Help() function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.

Dir() function: The dir() function is used to display the defined symbols.

```python

import os
help(os)
dir(os)
```

### Q37. How can the ternary operators be used in python?

```python
x = True if 5==5 else False
```

### Q38. What does this mean: `*args`, `**kwargs`? And why would we use it?

We use `*args` when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. `**kwargs` is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use `*bob` and `**billy` but that would not be wise.

### Q50. How is Multi-threading achieved in Python?

- [Processes and Threads - Microsoft](https://docs.microsoft.com/windows/win32/procthread/processes-and-threads)
- [Thread - Tech With Tim](https://youtu.be/olYdb0DdGtM)
- [Implementing Threading in Python 3 - Tech With Tim](https://youtu.be/cdPZ1pJACMI)
- [thread.py](src/thread.py)

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

### Q85. What is map function in Python?

map function executes the function given as the first argument on all the elements of the iterable given as the second argument. If the function given takes in more than 1 arguments, then many iterables are given. #Follow the link to know more similar functions.

- [Python's map() - realpython.com](https://realpython.com/python-map-function/)

```python

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

list(squared)
```

## [Python Interview Questions - InterviewBit](https://www.interviewbit.com/python-interview-questions/)

### 4. What is an Interpreted language?

An Interpreted language executes its statements line by line. Languages such as Python, Javascript, R, PHP and Ruby are prime examples of Interpreted languages. Programs written in an interpreted language runs directly from the source code, with no intermediary compilation step.

### 10. What are decorators in Python?

Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. They are represented by the `@decorator_name` in Python and are called in bottom-up fashion.

```python

# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper

@splitter_decorator  # this is executed next
@lowercase_decorator  # this is executed first
def hello():
    return 'Hello World'

hello()  # output => [ 'hello' , 'world' ]
```

The beauty of the decorators lies in the fact that besides adding functionality to the output of the method, they can even accept arguments for functions and can further modify those arguments before passing it to the function itself. The inner nested function, i.e. 'wrapper' function, plays a significant role here. It is implemented to enforce encapsulation and thus, keep itself hidden from the global scope

```python

# decorator function to capitalize names
def names_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return wrapper

@names_decorator
def say_hello(name1, name2):
    return 'Hello ' + name1 + '! Hello ' + name2 + '!'

say_hello('sara', 'smith')  # output => 'Hello Sara! Hello Smith!'
```

### 12. What are Dict and List comprehensions?

```python

my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
```

### 14. What is lambda in Python? Why is it used?

Lambda is an anonymous function in Python, that can accept any number of arguments, but can only have a single expression. It is generally used in situations requiring an anonymous function for a short time period. Lambda functions can be used in either of the two ways:

```python

mul = lambda a, b : a * b
print(mul(2, 5))  # output => 10

# Wrapping lambda functions inside another function
def myWrapper(n):
  return lambda a : a * n

mulFive = myWrapper(5)
print(mulFive(2))  # output => 10
```

## [Concurrency in Python - realpython.com](https://realpython.com/python-concurrency/)