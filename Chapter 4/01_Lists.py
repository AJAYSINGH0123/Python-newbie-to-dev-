# lists
"""Python lists are container to store a set of values of any data type"""
#Example:

friends = ["007","Ajay",7,True,"Rohan"]
print(friends)

# output = ['007', 'Ajay', 7, True, 'Rohan']
#can contain any data type including strings, integer, floating points number, boolean, etc.

print(friends[3])
print(friends[0:4]) # will exclude 'Rohan' and will print upto 'True'.

# Strings are immutable but... lists are not, So we can replace values inside a list
# for example:

friends[3] = False
print(friends[3])
# printing the whole list
print(friends)
# Lists are mutable