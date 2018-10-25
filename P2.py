

sum = 0
prev_number = 1
number = 1
while number <4000000:
    temp = number
    number = prev_number+number
    prev_number = temp
    if number%2==0:
        sum+=number

print(sum)
