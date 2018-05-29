def perfectnumber(num):
    sum=0
    for i in range (1,num):
        if num%i==0:
            sum=sum+i
    if num==sum:
        print(num,"is perfect")
    else:
        print(num,"is not perfect")
num=int(input("Enter any number:"))
perfectnumber(num)
