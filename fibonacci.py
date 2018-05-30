limit=int(input("Enter the limit of a series:"))
a=0
b=1
print(a)
print(b)
for i in range(limit-2):
    s=a+b
    print(s)
    a=b
    b=s
    
