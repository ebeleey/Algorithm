n, k = map(int, input().split())

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if k == 0:
    nCk = 1
elif n == k:
    nCk = 1
else: 
    nCk = factorial(n)//factorial(k)//factorial(n-k)
print(nCk)