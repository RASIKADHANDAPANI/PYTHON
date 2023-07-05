list=[]
n=int(input("enter no of element:"))
i=1
while i<=n :
    a= int(input())
    list.append(a)
    i+=1
l1=[]
for i in list:
    c=1
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                c=0
                break
        if(c==1):
            l1.append(i)
str=''
if(len(l1)>len(str)):
    print("True",l1)
else:
    print("False")
