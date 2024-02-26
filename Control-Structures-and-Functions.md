# Control Structures and Functions

## Control Structures
Control structures in Python allow you to dictate the flow of your program based on certain conditions. The main control structures in Python are:
Conditional Statements (if, elif, else): Used to execute different blocks of code based on specified conditions.
Loops (for, while): Allow you to iterate over a sequence of elements or execute a block of code repeatedly.
Conditional Statements
Conditional statements help you make decisions in your code based on specific conditions. The syntax for an if statement is as follows:
```python
# Example of if statement
x = 10
if x > 5:
    print("x is greater than 5")
```

You can also use elif and else statements to handle multiple conditions:
```python
# Example of if-elif-else statement
y = 3
if y > 5:
    print("y is greater than 5")
elif y == 5:
    print("y is equal to 5")
else:
    print("y is less than 5")
```

### Loops
Loops allow you to iterate over a sequence of elements or execute a block of code multiple times. The two main types of loops in Python are for and while loops.
For Loop
The for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each element:
```python
# Example of for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### While Loop
The while loop continues to execute a block of code as long as a specified condition is true:
```python
# Example of while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions
Functions in Python are blocks of reusable code that perform a specific task. They help you organize your code, make it more readable, and avoid repetition. Functions can take input parameters and return output values.
### Defining a Function
You can define a function using the def keyword followed by the function name and any parameters it takes:
```python
# Example of defining a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

### Calling a Function
To call a function and execute its code, simply use the function name followed by parentheses:
```python
# Example of calling a function
result = greet("Bob")
print(result)  # Output: Hello, Bob!
```

Functions can also have default parameters, variable-length arguments, and keyword arguments for added flexibility.
