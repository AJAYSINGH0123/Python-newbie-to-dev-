                                                    # Chapter-3
# Strings:
# String is a data type in python, it is a sequence of quotes enclosed in quotes
# We can primarily write string in three ways:
"""
1. a = 'happy'  single quoted string
2. b = "happy"  double quoted string
3. c = '''happy'''  triple quoted string
All three are correct methods to represent strings"""

# String Slicing
# A string in python can be sliced for getting a part of the string
# A string is immutable
# Once a string is created, you cannot change it, you cannot change a single character from a string.
# Example: 
        # Consider the following string:
name = "Happy"
sl = name[1:3]
print(sl)

# For String slicing we use: sl = name[ind_start:ind_end]
                                    #first index  #last index is not included
# Example:
name_ = "AJAYSINGH"
# string slicing
nameshort = name_[2:5]
character1 = name_[1]

print(nameshort)
print(character1)

#Slicing with skip value:-
# We can provide skip value as a part of our slice like this:
word = "amazing"
    # 1:6 --> jump->2
print(word[1:6:2])
print(word[:6])
