def palindrome(n):
    s=0
    m=n
    while n>0:
        a=n%10
        int(n)=n/10
        s=s*10+a
    if m==int(s):
        print("palindrome")
    else:
        print("not palindrome")

n=int(input("Enter any number:"))
palindrome(n)
