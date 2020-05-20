import math

sum = 0
num_people = 23
for i in range (1, num_people):
    one_case = 1
    for j in range (1, num_people):
        if i != j:
            one_case *= 365-j
        else:
            one_case *= i
    sum += one_case

sum *= 1/(math.pow(365, num_people-1))
print(sum)

# did not include the case of multiple collisions




