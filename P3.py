# Finds greatest prime factor
import time
from timeit import default_timer as timer
start = timer()

N=600851#475143
N=13195

candidates = range(1,N)

index= 1
gpf=1
while index<len(candidates):
#    print("No. candidates = ",len(candidates))
    current_candidate = candidates[index]
    #print('current candidate = ',current_candidate)
    if N%current_candidate==0:
        gpf=current_candidate
        temp = 0
        while candidates[temp]<=N/current_candidate:
            temp+=1
        candidates = candidates[0:temp]
    #Eliminate elements that are multiples of current candidate (they're not prime)
    candidates = [k for k in candidates if k%current_candidate!=0]
    #candidates = [k for k in candidates if k<N/current_candidate]
    #print('Current guess = ',gpf,'. Eliminating factors of',current_candidate,'leaves us with candidates =',candidates)

    # temp = 0
    # while candidates[temp]<=N/current_candidate-1:
    #     temp+=1
    # candidates = candidates[0:temp]
    #print('count = ',count)
    #print('current guess = ',gpf)


print (gpf)

end = timer()
print(end-start)
