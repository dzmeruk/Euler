import numpy
N=13195
N=15

# Need to think about prime numbers for a second...
# An approch from the bottom also limits the upper bound.
# If N is not divisible by two, the greatest prime factor must be less than N/2
# If it's not divisible by three, gpf must be less than N/3.
# So you only need to test up to sqrt(N)
# If it's not divisible by anything up to here, N is prime!

# Is there a faster method than brute force?

# If it's not div. by 2, we know it's not div. by any even number.

# First, I'll do complete brute force b/c the number they're interested in ain't toooooo big

# Nope, this method doesn't work (the gpf it finds is not guaranteed to be prime)

# Moving upwards, for every number that you pass, you can eliminate all multiples of that number

UB = numpy.sqrt(N).astype(int) # Upper bound

candidates = range(1,UB)
print(candidates)
current_candidate = 0

index = 0
#while current_candidate<UB:
while index<len(candidates):
    current_candidate = candidates[index]
    if N%current_candidate==0:
        gpf=current_candidate
    # Change candidate list to exclude all multiples of i
    candidates = [k for k in candidates if k%current_candidate!=0]
    print(current_candidate)
    print(candidates)
    index +=1
    # indices_to_keep = range(len(candidates))
    # for k in range(len(candidates)):
    #     if candidates[k]%current_candidate=0:
    #         indices_to_keep.remove(k)
    # candidates =



if gpf==1:
    gpf=N

print(gpf)
