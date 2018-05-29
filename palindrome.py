def palindrome(n):
    m=n
    r=0
    while(n>0):
        a=n%10
        r=r*10+a
        n=n//10
    if(m==r):
        print("The number is a palindrome!")
    else:
        print("The number is not a palindrome!")
n=int(input("Enter any number:"))
palindrome(n)
