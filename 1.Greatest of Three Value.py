a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
if(a>b and a>c):
    greater=a
elif(b>a and b>c):
    greater=b
else:
    greater=c
print("The greatest value is : ",greater)
