sub1 = int(input("Enter subject 1 marks : "))
sub2 = int(input("Enter subject 2 marks : "))
sub3 = int(input("Enter subject 3 marks : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You Failed the exams ")
elif(sub1 + sub2 + sub3)/3 <40:
    print("You failled due to not having reached a 40% of aggregate ")
else:
    print("Congratulations, You have successfully passed the exams")