# Problem Statement 3
name = "to check double  space in a string"
print(name.find("  "))

# Problem Statement 4
# to replace double spaces from the code with single spaces
string = "To  check  for double  spaces in your string"
print(string.replace("  ", " "))

# However the string is immutable; that is the string stored in variable 'name' won't change instead a new string will be made.
print(string)
print(name)
# Problem Statement 5

Letter = "Dear Harry, this python course is nice. Thanks!"
print("Dear Harry,\nThis python course is nice. \nThanks!")
print(Letter)