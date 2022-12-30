a=input("Enter a character to be checked for Upper or Lower case : ")
x=ord(a)
if(x>=65 and x<=90):
    print("The character is UPPERCASED !")
elif(x>=97 and x<=122):
    print("The given character is LOWERCASED")
else:
    print("Enter a Character !!!")
    
#Enter a character to be checked for Upper or Lower case : a
#The given character is LOWERCASED
#Enter a character to be checked for Upper or Lower case : A
#The character is UPPERCASED !