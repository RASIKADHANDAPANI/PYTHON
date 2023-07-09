def rec(n):
    if n<=1:
        return n
    else:
        return(rec(n-1)+rec(n-2))
n=int(input("enter terms:"))
list=[]
for i in range(n):
               list.append(rec(i))
a=max(list)
print(a)
               
