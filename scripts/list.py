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

