list=[]
n=int(input("enter no of element:"))
i=1
while i<=n :
    a= int(input())
    list.append(a)
    i+=1
c=int(input("enter the element to be searched:"))
index=[]
i=0
while i<len(list):
    if c==list[i]:
        index.append(i)
    i+=1
print("Positive index:",index)
ni=[]
for i in index:
    d=i-len(list)
    ni.append(d)
print("Negative index:",ni)
print("the Element appears",len(index),"times in list")
        
    
