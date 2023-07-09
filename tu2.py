tuple=('p','y','t','h','o','n')
str=""
for i in tuple:
    str+=i
t=()
for i in str[::-1]:
    t+=(i,)
print(t)
