"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines 
of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Input Format:

The first line contains an integer, denoting the number of commands.
N = 4

Second line onwards contains the list commands, one per line.
append 1
append 2
insert 1 3
print

Output:
[1, 3, 2]
"""

N = int(input())
ls = []
for _ in range(N):
    command = input().split() # split the input string into a list of strings
    if command[0] == "insert":
        ls.insert(int(command[1]), int(command[2]))
    elif command[0] == "append":
        ls.append(int(command[1]))
    elif command[0] == "remove":
        ls.remove(int(command[1]))
    elif command[0] == "append":
        ls.append(int(command[1]))
    elif command[0] == "sort":
        ls.sort()
    elif command[0] == "pop":
        ls.pop()
    elif command[0] == "reverse":
        ls.reverse()
    else:
        print(ls)
