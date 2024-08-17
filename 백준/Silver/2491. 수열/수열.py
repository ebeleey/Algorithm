N = int(input())
num = list(map(int, input().split()))

increase = [1] * N
decrease = [1] * N
for i in range(N-1):
    if num[i] < num[i+1]:
        increase[i+1] += increase[i]
    elif num[i] > num[i+1]:
        decrease[i+1] += decrease[i]
    else:
        increase[i+1] += increase[i]
        decrease[i+1] += decrease[i]

print(max(max(increase), max(decrease)))