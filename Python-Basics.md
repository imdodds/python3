# Python Basics

## Variables
In Python, variables are used to store data values. They act as placeholders for various types of data such as numbers, strings, lists, etc. When you assign a value to a variable, Python creates a reference to that value in memory. Variables can be reassigned with new values during the program execution.
```python
# variable reassignment
x = 5
print(x)  # Output: 5

x = x + 1
print(x)  # Output: 6
```

Variables in Python are dynamically typed, meaning you don't need to explicitly declare the data type of a variable. Python infers the data type based on the value assigned to it.

## Data Types
Python has several built-in data types that you can use to represent different kinds of information:
Integers (int): Whole numbers without decimal points.
Floats (float): Numbers with decimal points.
Strings (str): Sequences of characters enclosed in single or double quotes.
Booleans (bool): Represents True or False values.
```python
# different data types
num = 10
pi = 3.14
message = "Hello, World!"
is_true = True
```

Python also provides complex numbers, lists, tuples, dictionaries, and sets as additional data types for more advanced programming needs.

## Basic Operations
Python supports various basic operations that you can perform on variables and values:

### Arithmetic Operations:
Arithmetic operations allow you to perform mathematical calculations such as addition, subtraction, multiplication, division, etc.
```python
# Example of arithmetic operations
result_addition = 10 + 5
result_division = 20 / 4
result_exponentiation = 2 ** 3
```

### Comparison Operations:
Comparison operations are used to compare values and return a Boolean result (True or False).
```python
# Example of comparison operations
is_equal = 10 == 5
is_greater_than = 20 > 15
```

### Logical Operations:
Logical operations are used to combine multiple conditions and evaluate them to produce a single Boolean result.
```python
# Example of logical operations
result_and = True and False
result_or = True or False
result_not = not True
```