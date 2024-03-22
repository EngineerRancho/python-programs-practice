myDic = {
    "Fast" : "In a quick manner", # Dictionary with meanings defined 
    "Gaurav" : "A coder",
    "Marks" : [1, 2, 5],
    "AnotherDic" : {'Panditg' : 'Gaurav'}

}
# print(myDic.keys())  #prints the keys of the Disctionary
# print(myDic.values())  # prints the values of keys in the dictionary
# print(type(myDic.keys)) # Default datatype
# print(list(myDic))  # Change default data type bby type casting

print(myDic)
updateDic = {
    "Aridaman" : "Friend",
    "Nandan": "friend",
    "chaman" : "Unnkown",
    "Gaurav" : " the Rockstar"


}
myDic.update(updateDic)
print(updateDic["Nandan"]) #access through sub dictionary
print(myDic["chaman"])  # access through parent Dictionary
print(updateDic)   #updates the previous meaning 
# print(list(myDic.items))  #TypeError: 'builtin_function_or_method' object is not iterable 

print(myDic.get("gaurav"))  #return none because gaurav is not in the dictionary
print(myDic["Gaurav"])  # prints value associated with that key

# the .get method avoids the key error   