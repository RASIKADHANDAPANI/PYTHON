list=[]
n=int(input("enter no of words:"))
i=1
while(i<=n):
    a=input()
    list.append(a)
    i+=1
str=''
for i in list:
    if (len(i)> len(str)):
        str=i
print(str)
    
