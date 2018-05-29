num=int(input("Enter any number:"))
arm=0
n=num
while n>0:
    a=n%10
    arm=arm+a**3
    n=n//10
if arm==num:
    print("Armstrong number")
else:
    print("Not a armstrong number")
