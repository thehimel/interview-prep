# Python Interview Questions

## [Top 100 Python Interview Questions You Must Prepare In 2021 - www.edureka.co](https://www.edureka.co/blog/interview-questions/python-interview-questions/)

### Q28 What are the generators in python?

[Link](https://www.programiz.com/python-programming/generator)

- There is a lot of work in building an iterator in Python.
  - We have to implement a class with `__iter__()` and `__next__()` method.
  - Keep track of internal states, and raise `StopIteration` when there are no values to be returned.
- This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

- Python generators are a simple way of creating iterators.
- All the work we mentioned above are automatically handled by generators in Python.
- It is fairly simple to create a generator in Python.
- It is as easy as defining a normal function, but with a `yield` statement instead of a `return` statement.

### Q32. What are docstrings in Python?

- Docstrings are not actually comments, but, they are documentation strings.
- These docstrings are within triple quotes.
- They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.
- Often used to add some documentation about a class or function.

```python
def get_sum(x, y):
  """
  Function to return the sum of 2 numbers.
  :param x: int
  :param y: int
  :rtype: int
  """
  
  return x + y
```

### Q34. What is the usage of help() and dir() functions in Python?

- `help()` and `dir()` are used for viewing a consolidated dump of built-in functions.
- `help()` is displays the `docstring` and shows the help related to modules, keywords, attributes, etc.
- `dir()` is used to display the defined symbols.

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

- We use `*args` when we are not sure how many arguments are going to be passed to a function, or if we want to pass
a stored list or tuple of arguments to a function.
- `**kwargs` is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to
- pass the values of a dictionary as keyword arguments.
- The identifiers args and kwargs are a convention, `*bob` and `**billy` can also be used, but that would not be wise.

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

print(f"Total threads = {threading.active_count() }") # Total threads = 5
```

### Q85. What is map function in Python?

- The map function takes 2 arguments.
- The 1st arg is a function and the 2nd arg is an iterable (ex. list).
- The function is applied on every element of the iterable and the resulting iterable (ex. list) is returned.
- If the function given takes in more than 1 arguments, then many iterables are given.
- [Python's map() - www.realpython.com](https://www.realpython.com/python-map-function/)

```python
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

list(squared) # Output: [1, 4, 9, 16, 25]
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

- The beauty of the decorators lies in the fact that besides adding functionality to the output of the method, they can
- even accept arguments for functions and can further modify those arguments before passing it to the function itself.
- The inner nested function, i.e. 'wrapper' function, plays a significant role here.
  - It is implemented to enforce encapsulation and thus, keep itself hidden from the global scope

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

- Lambda is an anonymous function that can accept any number of arguments, but can only have a single expression.
- It is generally used in situations requiring an anonymous function for a short time period.
- Lambda functions can be used in either of the two ways:

```python
mul = lambda a, b: a * b
print(mul(2, 5))  # output => 10


# Wrapping lambda functions inside another function
def my_wrapper(n):
  return lambda a: a * n


mulFive = my_wrapper(5)
print(mulFive(2))  # output => 10
```

## [Concurrency in Python - www.realpython.com](https://www.realpython.com/python-concurrency/)

## Specific Questions from My Interview Experiences

### What are the differences between 'is' and '=='?

Difference between identity operator (is) and the equality operator (==).

Source: [Comparing Python Objects the Right Way: "is" vs "=="](https://realpython.com/courses/python-is-identity-vs-equality)

- The `==` operator compares the value or equality of two objects.
- The `is` operator checks whether two variables point to the same object in memory.
- This means you should use the equality operators == and !=, except when you are comparing to None.

Source: [Identity operators](https://geek-university.com/python/identity-operators/)

### Identity Operators

- The identity operators in Python are used to determine whether a value is of a certain class or type.
- They are usually used to determine the type of data a certain variable contains.
- For example, the identity operators can be combined with the `type()` function to ensure the specific variable type.

#### Two identity operators are available in Python:

- `is` returns True if the type of the value in the right operand points to the same type in the left operand.
  - For example, `type(3) is int` evaluates to `True` because `3` is indeed an `integer number`.
- `is not` returns True if the types of the values of the operands are different.
  - For example, `type(3) is not float` evaluates to `True` because `3` is not a `floating-point value`.

```pycon
>>> x = 5
>>> type(x) is int
True
>>> type(x) is not float
True
>>> y = 3.23
>>> type(y) is not float
False
>>> type(y) is int
False
```

### What are the differences between type() and isinstance()?

Source: [type() vs. isinstance()](https://switowski.com/blog/type-vs-isinstance)

- type only returns the type of object (its class). We can use it to check if variable is of a type `str`.
- isinstance checks if a given object (first parameter) is:
  - an instance of a class specified as a second parameter. For example, is variable an instance of the str class?
  - or an instance of a subclass of a class specified as a second parameter.
  - In other words - is variable an instance of a subclass of str?
  
#### Example
- Let’s say we want to have a custom class that acts like a list but has some additional methods.
- So we might inherit the `list` type and add custom functions inside `MyAwesomeList`.
- But now the type and isinstance return different results if we compare this new class to a list!
- The superclass of `my_list` is `list`. Thus, `isinstance(my_list, list)` is `True`.
- But the type of `my_list` is not `list`.

```python
class MyAwesomeList(list):
    # Add additional functions here
    pass

my_list = MyAwesomeList()

print(isinstance(my_list, list)) # True
print(type(my_list) is list) # False

print(type(my_list)) # <class '__main__.MyAwesomeList'>
```

### What will be the out of the following code snippet?

```python
class Dog:
  @staticmethod
  def bark():
    return "The dog is barking!"

  @staticmethod
  def eat():
    return "The dog is eating!"


class Cat:
  @staticmethod
  def bark():
    return "The cat is barking!"

  @staticmethod
  def eat(food):
    return f"The cat is eating {food}!"


class Hybrid(Dog, Cat):
  def eat(self):
    return "The animal is eating!"


animal = Hybrid()

print(animal.bark())
# print(animal.eat('meat'))
```

```text
The dog is barking!
Traceback (most recent call last):
  File "run.py", line 22, in <module>
    print(animal.eat('meat'))
TypeError: eat() takes 1 positional argument but 2 were given
```

- Both of the classes Dog and Cat have the bark() method. Both are inherited in Hybrid class.
- The method of the first passed class is considered. Even though the number of arguments are not matched.
- Output: `The dog is barking!`
  - In the case of eat(), it is defined in all the classes. But the method of Dog is called here.
- Output: `TypeError: eat() takes 1 positional argument but 2 were given`
  - Here the 2 positional arguments self and 'meat' are passed.

### What are the differences between list and array in Python. Which one is more efficient?

#### Sources

- [Array vs. List in Python](https://learnpython.com/blog/python-array-vs-list/)
- [Python List vs. Array - when to use?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)
- [Python Array](https://www.programiz.com/python-programming/array)

#### List and Array

List and array are ordered, mutable, enclosed in square brackets, and able to store non-unique items.

#### List vs. Array

- In list, elements can be of different data types.
- In array, elements must be of same data type.

#### Which one is more efficient?

Array is more efficient.

```python
my_list = [3, 6, 9, 12]
print(my_list)
print(type(my_list))
```

```text
[3, 6, 9, 12]
<class 'list'>
```

```python
import array as arr
import numpy as np

# built-in python array
# i stands for integer.
py_array = arr.array("i", [3, 6, 9, 12])
print(py_array)
print(type(py_array))

# array with numpy
numpy_array = np.array(["numbers", 3, 6, 9, 12])
print(numpy_array)
print(type(numpy_array))
```

```text
array('i', [3, 6, 9, 12])
<class 'array.array'>

['numbers' '3' '6' '9' '12']
<class 'numpy.ndarray'>
```


### What is the Global Interpreter Lock (GIL) in Python? How to deal with GIL?

Source - https://realpython.com/python-gil/

#### Global Interpreter Lock (GIL)

- GIL is a lock that allows only one thread to hold the control of the Python interpreter.
- This means that only one thread can be in a state of execution at any point in time.
- The impact of the GIL is not visible to developers who execute single-threaded programs, 
but it can be a performance blockage in CPU-bound and multi-threaded code.
- Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one
CPU core, the GIL has gained a reputation as an `infamous` feature of Python.

#### The Impact on Multi-Threaded Python Programs

```python
# single_threaded.py

import time

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)  # Time taken in seconds - 6.20024037361145
```

```python
# multi_threaded.py

import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)  # Time taken in seconds - 6.924342632293701
```

- As you can see, both versions take almost same amount of time to finish.
- In the multi-threaded version the GIL prevented the CPU-bound threads from executing in parallel.
- The GIL does not have much impact on the performance of I/O-bound multi-threaded programs as the lock is shared
between threads while they are waiting for I/O.
- But a program whose threads are entirely CPU-bound, e.g., a program that processes an image in parts using threads,
would not only become single threaded due to the lock but will also see an increase in execution time,
as seen in the above example, in comparison to a scenario where it was written to be entirely single-threaded.
- This increase is the result of acquire and release overheads added by the lock.

#### How to deal with GIL?

##### Multi-processing vs multi-threading

- The most popular way is to use a multi-processing approach where you use multiple processes instead of threads.
- Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem.
- Python has a multiprocessing module which lets us create processes easily like the below code snippet.

```python
from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start) # Time taken in seconds - 4.060242414474487
```

### How to Get Information About an Exception?

Source: https://docs.python.org/3/library/sys.html

#### sys.exc_info()

- This function returns a tuple of three values that give information about the exception that is currently being handled.
- If no exception is being handled anywhere on the stack, a tuple containing three None values is returned. Otherwise,
the values returned are (type, value, traceback). Their meaning is: type gets the type of the exception being handled
(a subclass of BaseException); value gets the exception instance (an instance of the exception type); traceback gets a
traceback object which encapsulates the call stack at the point where the exception originally occurred.
- Examples: https://www.programcreek.com/python/example/59/sys.exc_info
