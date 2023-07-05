l=[9,3,5,6,2,7,3,5,1,8]
l2=[]
a=len(l)
for i in range(0,a):
    if l[i] not in l2:
        l2.append(i)
print(l2)
