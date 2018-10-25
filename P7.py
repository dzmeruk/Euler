# Find the 10001st prime number

# I'm thinking something similar to the candidate list, but that won't work because I don't have an upper bound
# I'll try it anyway...

UB = 1000000 # Upper bound

candidates = range(2, UB)
index = 0
for i in range(2,UB):
    number=i
    temp=i-2
    while temp<(len(candidates)-number):
        temp+=number
        candidates[temp]=0

#print(candidates)
primes = [k for k in candidates if k!=0]
print(max(primes),' is the ',len(primes),'th prime.')
print("Which prime would you like? (n must be less than the number of this prime)")
n = input('n = ')
print (n,'th prime is ',primes[n-1])
