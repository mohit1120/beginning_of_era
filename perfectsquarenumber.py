num=int(input("Enter any number:"))
f=0
for i in range(num//2+1):
    if i*i==num:
        f=1
if f==1:
    
    print("Perfect square number")
else:
    print("Not a perfect square number")
