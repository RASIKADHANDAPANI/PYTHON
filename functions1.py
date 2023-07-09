#Write a python code which checks whether the input number is a Perfect Square or not using a function
def square(n):
    i=1
    while(i<n):
        if(i**2==n):
            return 0
        i+=1
    
n=int(input("enter a number:"))
c=square(n)
if c==0:
    print("Is a Square")
else:
    print("Not Square")
