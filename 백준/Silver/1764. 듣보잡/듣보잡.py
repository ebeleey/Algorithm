N, M = map(int, input().split())

# 듣도 못한 사람
notlisten = set(input() for _ in range(N))
notsee = set(input() for _ in range(M))

notlistenandsee = notlisten.intersection(notsee)

notlistenandsee = list(notlistenandsee)
notlistenandsee.sort()

print(len(notlistenandsee))
print(*notlistenandsee, sep='\n')