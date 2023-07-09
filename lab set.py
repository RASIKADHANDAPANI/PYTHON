set1=set()
set2=set()
n=int(input("enter no of elements in set 1:"))
i=1
while i<=n:
    e=int(input())
    set1.add(e)
    i+=1
a=int(input("enter no of elements in set 2:"))
c=1
while c<=a:
    e=int(input())
    set2.add(e)
    c+=1
z=set1&set2
if z==set2:
    print("True")
else:
    print("False")
