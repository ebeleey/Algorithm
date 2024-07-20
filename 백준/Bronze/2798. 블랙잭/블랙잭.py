from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

combis = list(combinations(nums, 3))

distance = 0
min_distance = 0
first_flag = True

for combi in combis:
    distance = M - sum(combi)
    if distance >= 0:
        if(first_flag == True):
            min_distance = distance
            result = sum(combi)
            first_flag = False
        else:  
            if(min_distance>distance):
                min_distance = distance
                result = sum(combi)

print(result)