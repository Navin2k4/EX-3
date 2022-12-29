m1=int(input("Enter Mark 1 M1 :"))
m2=int(input("Enter Mark 2 M2 :"))
m3=int(input("Enter Mark 3 M3 :"))
m4=int(input("Enter Mark 4 M4 :"))
m5=int(input("Enter Mark 5 M5 :"))
total=m1+m2+m3+m4+m5
avg=total/5
print("Your total is "+ str(total) + " Average is " + str(avg))
if(avg>=90):
    print("Your grade is O !")
elif(avg>=80 and avg<90):
    print("Your grade is A+ !")
elif(avg>=70 and avg<80):
    print("Your grade is A !")
elif(avg>=60 and avg<70):
    print("Your grade is B+!")
elif(avg>=50 and avg<60):
    print("Your grade is B !")
else:
    print("Your grade is U !")

