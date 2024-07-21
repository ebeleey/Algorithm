num_1, num_2 = map(int, input().split())

#최대공약수

a = max(num_1,num_2) # a>b
b = min(num_1, num_2)

gcd = 0
rem = 0

while (b != 0):
    rem = a % b
    a = b
    b = rem
gcd = a

# 최소공배수
# 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.

a = max(num_1,num_2) # a>b
b = min(num_1, num_2)

lcm = a * b // gcd

print(gcd, lcm)