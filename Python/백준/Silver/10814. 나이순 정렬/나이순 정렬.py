N = int(input()) #온라인 저지 회원의 수
members=[[] for _ in range(N)]
for i in range(N):
    age, name = input().split()
    members[i] = [int(age), name]
members.sort(key = lambda x:x[0])
for member in members:
    print(*member)