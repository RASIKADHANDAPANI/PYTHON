list=[]
n=int(input("enter no of element:"))
i=1
while i<=n :
    a= int(input())
    list.append(a)
    i+=1
list2=[]
list2=sorted(list)
c=1
for i in range(0,len(list)-1):
    if list[i]==list2[i]:
        c=1
    else:
        c=0
        break
if c==0:
    print("List is not in ascending order")
else:
    print("List is in ascending order")
