# Exception Handling

### Try-Except Blocks:
 - **Purpose**: try-except blocks allow you to handle potential errors that may occur during program execution.
 - **Functionality**: The code within the try block is executed, and if an exception is raised, it is caught by the corresponding except block.
 - **Benefits**: This mechanism prevents the program from crashing and provides a way to gracefully manage errors.

```python
try:
    result = 10 / 0  # Attempting division by zero
except ZeroDivisionError as e:
    print("Error: Division by zero")
```

### Handling Specific Exceptions:
 - **Customization**: By specifying different except blocks for specific exception types, you can tailor error handling based on the type of error that occurs.
 - ***Example***: In the case of a ZeroDivisionError, you can provide a specific message or action to handle this particular type of error.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Division by zero")
```

### Finally Block:
 - **Cleanup Operations**: The finally block is used for code that should always run, regardless of whether an exception is raised or not.
 - **Usage**: It is commonly employed for releasing resources, closing files, or performing cleanup tasks that need to be executed under all circumstances.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Division by zero")
finally:
    print("Cleanup operations")
```

## Debugging Techniques

### Print Statements:
 - **Debugging Aid**: Inserting print statements at strategic points in your code helps track the flow of execution and monitor the values of variables.
 - **Benefits**: Print statements are simple yet effective tools for understanding program behavior and identifying issues during runtime.

```python
x = 10
print("Value of x:", x)
```

### Using Debugger (pdb):
 - **Interactive Debugging**: The pdb module provides an interactive debugger that allows you to pause execution, inspect variables, set breakpoints, and step through code.
 - **Functionality**: It offers a more advanced debugging experience compared to print statements, enabling detailed analysis of program state and behavior.

```python
import pdb

def divide(x, y):
    result = x / y
    return result

pdb.set_trace()   # Set a breakpoint
result = divide(10, 0)
```

### Logging:
 - **Logging Levels**: The logging module enables logging messages at different levels (debug, info, warning, error, critical) to track program execution and monitor application behavior.
 - **Advantages**: Logging provides a systematic way to record events, errors, and information during program execution for debugging and analysis purposes.

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def some_function():
    logging.debug('This is a debug message')
    # More code here
```