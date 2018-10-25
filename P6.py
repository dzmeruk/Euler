N=100

sum1=0
sum2=0
for i in range(1,N+1):
    sum1+=i**2
    sum2+=i

sum2=sum2**2

print(sum1,sum2,abs(sum1-sum2))
