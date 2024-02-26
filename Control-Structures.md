# Control Structures and Functions

## Control Structures
Control structures in Python allow you to dictate the flow of your program based on certain conditions. The main control structures in Python are:
 - **Conditional Statements (if, elif, else)**: Used to execute different blocks of code based on specified conditions.
 - **Loops (for, while)**: Allow you to iterate over a sequence of elements or execute a block of code repeatedly.

### Conditional Statements
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

### For Loop
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

### Nested Loops
Nested loops in Python refer to the situation where one loop is present inside another loop. This allows for more complex iterations over multiple sequences or patterns. Nested loops are commonly used when you need to iterate over elements in a multidimensional data structure like a list of lists or a matrix.
```python
# Example of nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

In the above example:
 - The outer loop iterates over values from 0 to 2 (inclusive) with `i`.
 - For each value of `i`, the inner loop iterates over values from 0 to 1 (inclusive) with `j`.
 - The `print` statement displays the current values of `i` and `j` within each iteration.

### Nested Loops with Lists:
Nested loops are often used to iterate over elements in nested lists or multidimensional arrays. This allows you to access and manipulate individual elements at different levels of nesting.
```python
# Example of nested loops with lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next line after each row
```

In this example:
 - The outer loop iterates over each row in the `matrix`.
 - The inner loop iterates over each element within the current row.
 - The print statement displays each element horizontally within a row and moves to the next line for the next row.

### Control Flow Statements
Control flow statements like `break`, `continue`, and `pass` provide additional control over loop execution.
 - `break`: Exits the current loop prematurely.
 - `continue`: Skips the rest of the current iteration and continues with the next iteration.
 - `pass`: Does nothing and acts as a placeholder when no action is needed.
```python
# Example of control flow statements
for i in range(5):
    if i == 3:
        break  # Exit the loop when i equals 3
    elif i == 1:
        continue  # Skip printing when i equals 1
    else:
        pass  # Placeholder for future code implementation
    print(i)
```