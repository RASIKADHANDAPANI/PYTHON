
def si(p,n,r):
    si=(p*n*r)/100
    return si
name=input("enter your name:")
age=int(input("age:"))
g=(input("gender:"))
p=int(input("principal of interest:"))
n=int(input("year:"))
temp=0
if(g=='F'):
    if (age<=60):
        temp=12
        res=si(p,n,temp)
    else:
        temp=10
        res=si(p,n,temp)
else:
    if (age<=60):
        temp=12
        res=si(p,n,temp)
    else:
        temp=9
        res=si(p,n,temp)
print(res)
    
    
