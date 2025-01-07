X = int(input())

sum = 64
shortest = 64
n = 1

for i in range(7):
  if(sum == X):
    break
  elif(sum > X):
    shortest /= 2
    n+=1
    if(sum-shortest >= X):
      sum -=shortest
      n-=1
      

print(n)