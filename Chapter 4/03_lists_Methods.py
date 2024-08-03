List = ["Ajay", 2.6, "Arya", 7, True, "007", 264, "Rohit"]
print(List)

# methods

List.append("Baddy") #l.append():adds a value at the end
print(List) 

L = [1, 34, 45, 3, 5, 11]
L.sort() #sorts the list in ascending order
print(L)

L1 = [2, 4, 56, 23, 11, 5]
L1.reverse() # reverses the whole list
print(L1)

L1.insert(3,8) # adds 8 at the index 3
print(L1) # L1 = [5, 11, 23, 8, 56, 4, 2]

L1.pop(2)  # Will delete element at index 2-- L1 = [5, 11, 23, 8, 56, 4, 2]
print(L1)  # new list L1 = [5, 11, 8, 56, 4, 2]

L1.remove(56)  # Will remove 56 from the list 
print(L1)