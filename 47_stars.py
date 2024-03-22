# printing the stars 

n = 4

for i in range(4):
    print("*" *(i+1))
    
    
# printing the stars with spaces

n = int(input("Enter the number of stars sequence to be printed : "))
for i in range (n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))


# print the series with irregular spaces and stars

# a = 2
# for i in range(3):
#     if i == 2:
#         print(" " * (i+1))             #incorrect 
#         continue
#     else:
#         print("*")
    