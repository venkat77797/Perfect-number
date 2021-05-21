def perfect_number(num,sum=1):
    n=num
    for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                sum+=i
                sum+=(num//i)
    if(sum==n):
        print("Perfect number")
    else:
        print("not a perfect number")


num=int(input())
perfect_number(num)
