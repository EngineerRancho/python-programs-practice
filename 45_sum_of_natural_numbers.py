# numB = int(input("Enter the Begining of numbers :"))
# numE = int(input("Enter the End Range of numbers :"))
# i = numB
# while i<=numE:
#     numB = numB +1
#     print(f"Sum = {numB +i } ")
#     i = i+1


# first n natural numbers addition using while loop

a = int(input("Enter the number to start with :"))
n = int(input("enter the number to end with : "))
i = a
sum = 0
while (i <= n):
    sum = sum + i
    i = i + 1
print("The sum is: ", sum)