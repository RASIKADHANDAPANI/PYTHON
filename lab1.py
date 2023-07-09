
num=int(input("Enter number:"))
if(num%2!=0):
    count=0
    c=0
    f=1
    while(num>0):
            num//=10
            count+=1
    print(count)

    
    
else:
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
