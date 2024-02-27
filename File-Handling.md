# File Handling

### Opening a File:
 - The `open()` function is used to open files in different modes like read (`'r'`), write (`'w'`), append (`'a'`), or binary mode (`'b'`).
 - It's important to specify the correct file path and mode when opening a file.

### Reading from a File:
 - The `read()` method reads the entire content of the file as a string.
 - The `readline()` method reads a single line from the file.
 - The `readlines()` method reads all lines into a list.

```python
# Opening a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Writing to a File:
 - Use modes like `'w'` (write) or `'a'` (append) to write content to a file.
 - It's good practice to use the `with` statement to automatically close the file after writing.

```python
# Writing content to a file
with open('output.txt', 'w') as output_file:
    output_file.write("Hello, World!")
```

### Closing a File:
 - Always close the file using the `close()` method after reading or writing operations to free up system resources.

## Working with External Files

### Handling Exceptions:
 - Use `try-except` blocks to handle exceptions like `FileNotFoundError` that may occur during file operations.
 - Proper error handling ensures your program doesn't crash when dealing with files.

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals():
        file.close()
```

### Using Context Managers (with Statement):
 - Context managers, implemented with the `with` statement, ensure proper resource management and automatic closing of files.
 - They simplify code and help avoid common issues like forgetting to close files.

```python
# Using context managers for file handling
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Working with CSV Files (Comma-Separated Values):
 - The `csv` module provides functionality for reading and writing data in CSV format.
 - It allows you to work with structured data stored in CSV files efficiently.

```python
import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
```