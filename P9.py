# Subdivide 1000 into three pieces and look for pythagorean triples

def istriple(a,b,c):
    #numbers need not be in numerical order
    li=[a,b,c]
    li.sort
    if li[0]**2+li[1]**2==li[2]**2:
        return 1
    else:
        return 0


# How many sets are there of 3 integers that add to 1000?
N=1000

#[118][127][136][145][226][235][244][334]

#Not super efficient, but it'll do..
for i in range(1,N-2):
    for j in range(i,N-i-2):
        k=N-(i+j)
        if istriple(i,j,k)==1:
            print i,j,k
