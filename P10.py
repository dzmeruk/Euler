UB = 10#2000000 # Upper bound

candidates = range(2, UB)
index = 0
for i in range(2,UB):
    number=i
    temp=i-2
    while temp<(len(candidates)-number):
        temp+=number
        candidates[temp]=0

#print(candidates)
#primes = [k for k in candidates if k!=0]
print(sum(candidates))
