#  String Functions:
# len() function: this function returns the length of the strings.
# Example:
name = "Happy"
print(len(name))
# string.endswith(): This function tells whether the variable string ends with the string "ppy" or not.
# If string is "happy", it returns true for "ppy" since happy ends with ppy.
# Example: 
Mystring = "Happy"
print(Mystring.endswith("ppy"))
print(Mystring.startswith("a"))

#string.count("p"): Counts the total number of occurences of any character.
# Example: 
String = "Happy"
count = String.count("p")
print(count)

# string.capitalize()--> This function capitalizes the first character of a given string
# print(name.capitalize()): o/p-->Capital letter for first character

# string.find(word): This function finds the word and returns the occurence of first index of that word.
# Example: 
s = "Hello World"
index = s.find("World")
print(index) #o/p the index will be 6

# string.replace(old word.new word): This function replace the old word with the new word in the entire string.
# Example:
replaced_string = s.replace("World", "Python")
print(replaced_string)