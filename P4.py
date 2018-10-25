# There are only ~10^6 numbers under 999^2.  Couldn't I just brute force this?
# I'm guessing that's harder than I realize...

# Brute force method:
N=1000

def isPalindrome(x):
    if str(x)[::-1]==str(x):
        return 1
    else:
        return 0

winning_set = [1,1,1]
for i in range(1,N):
    for j in range(i,N):
        #print(i,j,i*j)
        if isPalindrome(i*j)==1:
            if i*j>winning_set[2]:
                winning_set=[i,j,i*j]

print(winning_set)
