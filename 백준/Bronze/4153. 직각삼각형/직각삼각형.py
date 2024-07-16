while(1):
  edges = list(map(int, input().split()))
  if(edges == [0,0,0]):
    break
  else:
    max_edge = max(edges)
    edges.remove(max_edge)
    sum = 0
    for i in range(2):
      sum += edges[i]**2
    if(max_edge**2==sum):
      print("right")
    else:
      print("wrong")
    
