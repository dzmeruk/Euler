from timeit import default_timer as timer
start = timer()

N=600851475143

x=N
divisor = 2
while x!=divisor:
    if x%divisor==0:
        x=x/divisor
    else:
        divisor+=1

print(x)

end = timer()
print(end-start)
