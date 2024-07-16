
while(1):
  a, b, c=map(int, input().split())
  abc = [a,b,c]
  if(abc == [0,0,0]):
    break
  else:
    Max = max(abc)
    abc.remove(Max)
    sum = 0
    for i in range(2):
      sum += abc[i]**2
    if(Max**2==sum):
      print("right")
    else:
      print("wrong")
    