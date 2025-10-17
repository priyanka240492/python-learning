"""
File: comprehension.py
Purpose: Demonstrate Python List and Dictionary Comprehensions 
Author: Priya K
Description:
    This module illustrates various real-world use cases of list and dictionary 
    comprehensions, including filtering, transformation, flattening, conditional logic, 
    and indexing with enumerate().
"""

# --------------------------------------------------------------------
# Input Data
# --------------------------------------------------------------------
emp_list = [
    {'name': 'priya', 'age': 25, 'dept': 'IT'},
    {'name': 'lakshmi', 'age': 20, 'dept': 'HR'},
    {'name': 'aarya', 'age': 20, 'dept': 'Finance'}
]

# --------------------------------------------------------------------
# Basic Filtering with List Comprehension
# --------------------------------------------------------------------
mylist1 = [emp for emp in emp_list if emp['age'] == 20]
print("Output as List (employees aged 20):", mylist1)

# Equivalent Expanded Code
mylist2 = []
for emp in emp_list:
    if emp['age'] == 20:
        mylist2.append(emp)
print("Equivalent Expanded List:", mylist2)

# --------------------------------------------------------------------
# Extract Specific Fields
# --------------------------------------------------------------------
names_under_25 = [emp['name'] for emp in emp_list if emp['age'] < 25]
print("List of employees under 25:", names_under_25)

# Dictionary of name → age (filter under 25)
name_age_map = {emp['name']: emp['age'] for emp in emp_list if emp['age'] < 25}
print("Name–Age mapping for employees under 25:", name_age_map)

# --------------------------------------------------------------------
# Inline conditional Expression inside Comprehension
# --------------------------------------------------------------------
age_group = {emp['name']: ('Young' if emp['age'] <= 22 else 'Experienced') for emp in emp_list}
print("Categorised employees:", age_group)

# --------------------------------------------------------------------
# Nested List Comprehension (Flattening)
# --------------------------------------------------------------------
departments = [['IT', 'HR'], ['Finance', 'Admin'], ['Marketing']]
flat_list = [dept for group in departments for dept in group]
print("Flattened Department List:", flat_list)

# --------------------------------------------------------------------
# Derived Computation Example
# --------------------------------------------------------------------
# Add 5 years to everyone's age
future_age = {emp['name']: emp['age'] + 5 for emp in emp_list}
print("Future Age after 5 years:", future_age)

# --------------------------------------------------------------------
# Filtering and Transformation Together
# --------------------------------------------------------------------
# Names of employees whose department starts with 'F'
filtered_names = [emp['name'].upper() for emp in emp_list if emp['dept'].startswith('F')]
print("Uppercase Names from Finance Department:", filtered_names)

# --------------------------------------------------------------------
# Nested Dictionary Comprehension
# --------------------------------------------------------------------
# Example: group by age
age_grouped = {age: [emp['name'] for emp in emp_list if emp['age'] == age] for age in {emp['age'] for emp in emp_list}
}
print("Grouped employees by age:", age_grouped)

# --------------------------------------------------------------------
# Combining enumerate() and conditional logic
# --------------------------------------------------------------------

"""
The enumerate() function attaches an index to each element of a list,
allowing you to access both the index and the element simultaneously.
"""

indexed_young_emp = {i: emp['name'] for i, emp in enumerate(emp_list, start=1) if emp['age'] < 25}
print("Indexed list of young employees:", indexed_young_emp)

# --------------------------------------------------------------------
# Summary Output
# --------------------------------------------------------------------
print("\n Demonstration of list & dict comprehensions complete.")
