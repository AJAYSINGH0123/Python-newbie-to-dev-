# /"Lists And Tuples/"

# Lists: Python lists are containers to store a set of value of any data type.
# For Example: 
friends = ["007", "Ajay", 7, "rohan", True]
print(friends)
print(friends[2])
# Can contain any data type including strings, integer, floating point numbers, boelean, etc.

# Strings are immutable but lists are not so we can replace values inside a list.
# for example: 
friends[3] = False
print(friends)

# List indexing and slicing is similar to strings
# For Example:
print(friends[0])
print(friends[3])
# Slicing
print(friends[0:3])
print(friends[0:5:2])