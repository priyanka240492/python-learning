"""
File: iteratorVsIterable.py
Purpose: Demonstrate the difference between Iterators and Iterables in Python
Author: Priya K

Description:
    This module illustrates various real-world use cases of iterators and iterables,
    including how to create and use them effectively.

    ▪ Iterator:
        - An object that doesn't store complete data in memory.
        - Produces items one by one as long as requested.
        - Use cases:
            • Efficient memory usage for large datasets.
            • Building a looping mechanism that can traverse data without loading it all at once.

    ▪ Iterable:
        - An object that contains a collection of data that can be iterated over.
        - Example: In a list, each element is an iterable item.
"""

# ==============================================================================
# 1. enumerate() → Listing iterables with their index position
# ------------------------------------------------------------------------------
# 💡 Use Case:
#     Find the exact position of bad data in your list or dataset.
# ==============================================================================

letters = ['a', 'b', 'c', 'd', 'e']
print("Position of each iterable item using enumerate():", list(enumerate(letters)))

for index, letter in enumerate(letters):
    print("Current Index position and Letter:", index, letter)


# ==============================================================================
# 2. reversed() → Returns an iterator that reverses the data order
# ------------------------------------------------------------------------------
# 💡 Use Case:
#     When you need to iterate backward over a sequence.
# ==============================================================================

print("Reversing list iterables using reversed():", list(reversed(letters)))

for letter in reversed(letters):
    print("Current Letter in reversed order:", letter)


# ==============================================================================
# 3. zip() → Combines two or more iterables into pairs of tuples
# ------------------------------------------------------------------------------
# 💡 Use Case:
#     To pair corresponding elements from multiple lists.
# ==============================================================================

numbers = [1, 2, 3, 4, 5]
print("Zipped result of letters and numbers:", list(zip(letters, numbers)))


# ==============================================================================
# 4. map() → Applies a function to all items in an iterable
# ------------------------------------------------------------------------------
# 💡 Use Cases:
#     • Perform transformation logic (e.g., square numbers).
#     • Convert data types such as strings to integers or vice versa.
# ==============================================================================

def square(num):
    return num * num

print("Squared numbers using map():", list(map(square, numbers)))


# ==============================================================================
# 5. filter() → Cleans up data by filtering unwanted items
# ------------------------------------------------------------------------------
# 💡 Use Cases:
#     • Remove invalid or unwanted data from lists.
#     • Keep only records matching a specific condition.
#
# | Expression           | Behaviour                                   | Keeps Elements That Are |
# | -------------------- | ------------------------------------------- | ----------------------- |
# | filter(None, list)   | Removes falsy items                         | Truthy values only      |
# | filter(func, list)   | Removes items where func(item) is False     | Function returns True   |
# ==============================================================================

age = [10, -5, 3, -1, 0, 7, -2]

def is_valid_age(a):
    return a >= 0

valid_ages = list(filter(is_valid_age, age))
print("Filtered valid ages using filter():", valid_ages)

ls = ["x", "y", "z", None, "xx"]
print("Filtered valid string values using filter():", list(filter(None, ls)))
