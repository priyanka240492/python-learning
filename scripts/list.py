######################### 1. Data Structure - List #########################

############### Creates empty list with square braces ##################
ls1 = [] 
print(type(ls1))

# Creates empty list with function list()
ls2 = list()
print(type(ls2))

# Manual creation with items
ls3 = [10,20,30,40,50,60] 
print(type(ls3))

# Nested list
ls4 = [['Priya','IT',2000],['Lakshmi','IT',3000]] 
print(type(ls4))

################# Access and Read List items #########################

# Get single item - Indexing
print(ls3[0])

# Get multiple items - Slicing
print(ls3[0:4])# Subracts 1 from given end index value - retrieves items of 0,1,2,3 index position

# Get matrix items
print(ls4[0][2]) # For matrix, list[row index][column index]

################### Unpack List ###############################

a,b,c,d,e,f = ls3 # Unpacking technique when no of variables match no of items
print(b)

aa,*bb = ls3 # Use * to store rest of the items in a seperate list
print(aa)
print(bb)

xx, *_, zz = ls3 # Use _ for ignoring the items without storing in memory
print(xx)
print(zz)

################# iloc while accessing dataframe #########################
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print(df)

# Accessing rows using iloc
print("Access 2nd Row", df.iloc[1]) # Access 2nd row
print("Access 1st to 3rd row", df.iloc[0:3]) # Access 1st to 3rd row. Last index is excluded.
print("Access 2nd row and 3rd column item", df.iloc[1,2]) # Access 2nd row and 3rd column item
print("Access 1st to 2nd row and 1st to 2nd column items", df.iloc[0:2, 0:2]) # Access 1st to 2nd row and 1st to 2nd column items

################# List Methods #########################
ls3.append(70) # Adds item at the end of the list
print(ls3)
ls3.insert(2,25) # Inserts item at the given index position
print(ls3)
ls3.remove(3, 40) # Removes the given item from the list
print(ls3)
ls3.pop() # Removes the last item from the list
print(ls3)
ls3.pop(1) # Removes item at the given index position
print(ls3)
ls3.sort() # Sorts the list in ascending order
print(ls3)
ls3.sort(reverse=True) # Sorts the list in descending order
print(ls3)
ls3.reverse() # Reverses the list
print(ls3)
print(ls3.count(30)) # Counts occurrences of an item in the list
print(ls3.index(50)) # Returns the index of the first occurrence of an item

