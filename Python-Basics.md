# Python Basics

## Variables
In Python, variables are used to store data values. They act as placeholders for various types of data such as numbers, strings, lists, etc. When you assign a value to a variable, Python creates a reference to that value in memory. Variables can be reassigned with new values during the program execution.
```python
# Example of variable reassignment
x = 5
print(x)  # Output: 5

x = x + 1
print(x)  # Output: 6
```

Variables in Python are dynamically typed, meaning you don't need to explicitly declare the data type of a variable. Python infers the data type based on the value assigned to it.

## Data Types
Python has several built-in data types that you can use to represent different kinds of information:
 - **Integers (int)**: Whole numbers without decimal points.
 - **Floats (float)**: Numbers with decimal points.
 - **Strings (str)**: Sequences of characters enclosed in single or double quotes.
 - **Booleans (bool)**: Represents True or False values.
```python
# Example of different data types
num = 10
pi = 3.14
message = "Hello, World!"
is_true = True
```

Python also provides complex numbers, lists, tuples, dictionaries, and sets as additional data types for more advanced programming needs.

### Mutability
Mutability refers to whether a data type's value can be changed after it has been created. In Python, some data types are mutable (can be changed) while others are immutable (cannot be changed).
Immutable Data Types: Integers, floats, strings, tuples are immutable. Once created, their values cannot be altered.
Mutable Data Types: Lists, dictionaries, sets are mutable. You can modify their values after creation.
```python
# Example of mutability with lists
num_list = [1, 2, 3]
num_list[0] = 10  # Lists are mutable
```

### Type Conversions
Type conversions allow you to convert one data type to another in Python using built-in functions like int(), float(), str(), bool().
```python
# Example of type conversions
num_str = "10"
num_int = int(num_str)
```

## Basic Operations
Python supports various basic operations that you can perform on variables and values:

### Arithmetic Operations:
Arithmetic operations allow you to perform mathematical calculations such as addition, subtraction, multiplication, division, etc.
 - Addition `+`
 - Subtraction `-`
 - Multiplication `*`
 - Division `/`
 - Modulus `%` (returns the remainder)
 - Exponentiation `**` (raises a number to a power)
```python
# Example of arithmetic operations
result_addition = 10 + 5
result_division = 20 / 4
result_exponentiation = 2 ** 3
```

### Comparison Operations:
Comparison operations are used to compare values and return a Boolean result (True or False).
 - Equal to `==`
 - Not equal to `!=`
 - Greater than `>`
 - Less than `<`
 - Greater than or equal to `>=`
 - Less than or equal to `<=`
```python
# Example of comparison operations
is_equal = 10 == 5
is_greater_than = 20 > 15
```

### Logical Operations:
Logical operations are used to combine multiple conditions and evaluate them to produce a single Boolean result.
 - AND `and`
 - OR `or`
 - NOT `not`
```python
# Example of logical operations
result_and = True and False
result_or = True or False
result_not = not True
```