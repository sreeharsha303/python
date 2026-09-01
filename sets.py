set = {"a","b","c",2,3,"hello",True,1,False}

print(type(set))

set.add("false")  # adds the element for the set

#update: add a ittarable for the set
set.update([1,2,3,4,5])

#remove: remove an element to the set if gives error if the item is not present 
set.remove("hello")

#discord:  remove an element to the set it not show the error if the iten not present in set
set.discard("c")

#clear

# del


#set operation

#union it merges the both sets 

set1 = {1,2,3}
set2 = {3,4,5}
print(set1)
print(set2)

print(set1|set2)

# intersection : return the common elements

print(set1.intersection(set2))

#difference : Difference returns elements that are present in the first set but not in the second set.

print(set1.difference(set2))

# Symmetric Difference : Returns elements that are in either set but not in both




#frozen set : this is immutable version of set
fs = frozenset([,1,2,3,4])
print(fs)
print(type(fs))






print(set)

