# Lists

Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable (modifiable), and can contain elements of different data types. Lists are created by placing comma-separated values within square brackets [ ].

### Creating Lists:
```python
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ['apple', 'banana', 'cherry']

# Creating a mixed-type list
mixed_list = [1, 'hello', True, 3.14]
```

### Accessing Elements:
Elements in a list are accessed using index numbers starting from 0.
Negative indices can be used to access elements from the end of the list.
```python
# Accessing elements in a list
print(numbers[0])  # Output: 1
print(fruits[-1])  # Output: 'cherry'
```

### List Operations:
 - **Appending**: Adding elements to the end of a list using the append() method.
 - **Inserting**: Inserting elements at a specific index using the insert() method.
 - **Slicing**: Extracting a subset of elements using slicing notation [start:stop:step].
 - **Concatenation**: Combining lists using the + operator.
 - **Repetition**: Repeating a list using the * operator.
```python
# List operations
fruits.append('orange')  # Append 'orange' to fruits list
numbers.insert(2, 10)    # Insert 10 at index 2 in numbers list
subset = fruits[1:3]      # Extract elements at index 1 and 2 from fruits list
combined_list = numbers + fruits  # Concatenate numbers and fruits lists
repeated_list = numbers * 3        # Repeat numbers list three times
```

### List Methods:
 - **append()**: Add an element to the end of the list.
 - **extend()**: Extend the list by appending elements from another iterable.
 - **insert()**: Insert an element at a specified position.
 - **remove()**: Remove the first occurrence of a value from the list.
 - **pop()**: Remove and return an element at a specified index.
```python
# List methods
fruits.append('grape')     # Append 'grape' to fruits list
numbers.extend([6, 7])     # Extend numbers list with [6, 7]
fruits.remove('banana')    # Remove 'banana' from fruits list
popped_element = numbers.pop(3)  # Remove and return element at index 3 from numbers list
```