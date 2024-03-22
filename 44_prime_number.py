Num = int(input("Enter the number : "))
prime = True
for i in range(2, Num):
    if(Num%i == 0):
        prime = False
        break
if prime:
    print("The given numebr is prime")
else:
    print("The given number is not prime")