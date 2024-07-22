T = int(input())

# a층의 b호에 살려면 
# 자신의 아래 a-1층의 1호부터 b호까지 사람들의 수의 합만큼 
# 사람들을 데려와 살아야 한다.

def how_many_people(floors, rooms):
    
    people = [[0] * (rooms + 1) for _ in range(floors + 1)]    
    
    for i in range(rooms+1):
        people[0][i]=i 
    if(floors>=1):
        for k in range(1, floors+1):
            for n in range(1, rooms+1):
                people[k][n] = sum(people[k-1][1:n+1])
    return people[floors][rooms]

for i in range(T):
    k = int(input())
    n = int(input())
    print(how_many_people(k, n))


