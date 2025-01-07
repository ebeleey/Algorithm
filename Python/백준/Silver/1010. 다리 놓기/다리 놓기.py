def factorial(k):
  result = 1
  for i in range(1, k+1):
    result *= i
  return result

n = int(input())

for i in range(n):
  westSite, eastSite = map(int,input().split())
  print(factorial(eastSite)//(factorial(eastSite-westSite)*factorial(westSite))) 

