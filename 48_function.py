# marks = [45, 64, 56, 87]
# percentage1 = (sum(marks)/4)

# marks2 = [75, 65, 49, 98]
# percentage2 = (sum(marks2)/4)
# print("",percentage1,"%", "\n",percentage2,"%")


# def percentage(marks):
    # a = int(input("rnter the number of subjects : "))
#    for i in range(1, len(marks)):
#        total = sum(marks)
#        print(f" The percentage marks obtained are : {total/len(marks)}")

# Function


def percentage(marks):
    p=(sum(marks)/len(marks))
    return p


marks1 = [90, 50, 80, 70, 60, 56, 57, 46 , 65]
marks2 = [90, 50, 80, 45, 70, 76, 87, 49 , 45]
percentage1 = percentage(marks1)
percentage2 = percentage(marks2)
print(f"{percentage1} % \n{percentage2} %")
# print(type(percentage1))

