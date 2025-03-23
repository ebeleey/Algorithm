N, d, k, c = map(int, input().split())

belt = [int(input()) for _ in range(N)]
belt = belt + belt

answer = 0
for i in range(N):
    sushi = set(belt[i:i+k])
    # print(sushi)
    sushi.add(c)
    answer = max(answer, len(sushi))

print(answer)