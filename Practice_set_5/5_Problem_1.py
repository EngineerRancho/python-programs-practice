MyDict = {
    "Pankha": "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"

}
print("Options are :", MyDict.keys())
a = input("Enter the Hindi Word : ")
# print("The meaning of your word is : ", MyDict[a])   # throws error when the key does not exist in the dictionary
print("The meaning of your word is : ", MyDict.get(a)) # without throwig error, 