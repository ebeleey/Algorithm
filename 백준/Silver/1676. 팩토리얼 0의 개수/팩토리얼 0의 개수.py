def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())
nums = str(factorial(N))[::-1]

count = 0
for num in nums:
    if num == '0':
        count += 1
    else:
        break

print(count)