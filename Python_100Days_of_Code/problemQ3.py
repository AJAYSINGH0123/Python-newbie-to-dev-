# Problem Statement:
# Problem to check double space in a string-->
# Write your code here:

name = " to check for double  spaces in the string"
print(name.find("  "))  # Index of the start of the double space
# If no double space present , o/p--> -1

# Problem Statement: replace the double spaces with single spaces:
print(name.replace("  ", " "))