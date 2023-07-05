odd=set([i**2 for i in range(1,31)])
set1=set()
for i in range(1,51):
    if i%3==0:
        set1.add(i)
print(odd-set1)
