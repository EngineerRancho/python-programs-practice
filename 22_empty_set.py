a = set()
b = {42, 435, 34, 2, 6, 23 , 5 ,23, 4,3, 4,5 , 34, 23, 422, 35, 2, 6, 52}
print(type(a))

a.add("a")
a.add(45)
a.add(78)
a.add(47)
a.add(47)
a.add(47)
a.add(47)           #Allows no repetations
a.add(43)
# a.add([2,5,6])      #list can not be inseted in the set
a.add((3,64,754))   #A tuple can be inserted into a set 
# a.add({4:5})        #Dictionary can not be added to the list
print(a) 

# Set is unindexed

print(len(a))   #prints the lenght of the set
a.remove("a")   #removes 'a' from set a

print(a) 
print(a.pop())      # pop and print any random arbitory element out of the set
# print(a.clear())    # Clear the set
print(a.union(b))       # Union of the set
print(a.intersection(b)) #intersection of the set

