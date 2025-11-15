                                # Chapter- 5 #
                            # /* Dictionary and sets */
# Dictionary is a collection of key value pairs
# Syntax: 
a = {"key" : "value", "Ajay" : "Codes", "Marks" : "100", "list" : [1, 2, 9]}
print(a)
print(a["key"])
print(a["list"])
# Properties of python dictionaries:
'''
1. It is un-ordered
2. It is mutable
3. it is indexed
4. Cannot contain duplucate keys '''

# Dictionary Methods: 
# Consider the following dictionary: 
d = {"name" : "Ajay", "From" : "India", "BMI" : [190, 45, 30]}
print(d.items()) # returns a list of key vakue tuples
print(d.keys()) # returns a list containing dictionary keys
d.update({"Friend" : "Sam"}) # updates the dictionary with given key value pairs
print(d.get("name")) # returns the value of the specified keys, (and the value is returned e.g. "Ajay" is retuned here).
print(d) 