odd=set()
for i in range(1,51):
    if i%2!=0:
        odd.add(i)
set1=set()
for i in range(1,51):
    c=1
    if(i>1):
        for j in range(2,i):
            if (i%j==0):
                c=0
                break
        if(c==1):
            set1.add(i)
print(odd|set1)
print(odd-set1)
print(odd&set1)
print(odd^set1)
