import numpy
import sys

# If M is a multiple of N, M%N=0
N=int(sys.argv[1])
count = 0
for i in range(N):
    if i%5==0:
        count+=i
    elif i%3==0:
        count+=i

print(count)
