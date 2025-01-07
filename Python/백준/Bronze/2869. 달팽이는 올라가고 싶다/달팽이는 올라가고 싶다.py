import math 

a, b, v = map(int, input().split())

meters = v - a
days = math.ceil(meters/(a-b))+1
print(days)
