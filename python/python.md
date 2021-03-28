# Python Interview Questions

## [Top 100 Python Interview Questions You Must Prepare In 2021 - Edureka](https://www.edureka.co/blog/interview-questions/python-interview-questions/)

### What are the generators in python?

[Link](https://www.programiz.com/python-programming/generator)

There is a lot of work in building an iterator in Python. We have to implement a class with `__iter__()` and `__next__()` method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a `yield` statement instead of a `return` statement.
