
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def is_same(arr, x, y, l):
    global bcnt, wcnt

    # 기저 조건
    arrset = set()

    for i in range(l):
        for j in range(l):
            arrset.add(arr[i][j])
    if arrset == {1}:
        bcnt += 1
    elif arrset == {0}:
        wcnt += 1

    else:
        nl = l//2

        newarr = [[0] * nl for _ in range(nl)]
        for i in range(nl):
            for j in range(nl):
                newarr[i][j] = matrix[x+i][y+j]
        is_same(newarr, x, y, nl)

        newarr = [[0] * nl for _ in range(nl)]
        for i in range(nl):
            for j in range(nl):
                newarr[i][j] = matrix[x+i][y+nl+j]
        is_same(newarr, x, y+nl, nl)

        newarr = [[0] * nl for _ in range(nl)]
        for i in range(nl):
            for j in range(nl):
                newarr[i][j] = matrix[x+nl+i][y+j]
        is_same(newarr, x+nl, y, nl)

        newarr = [[0] * nl for _ in range(nl)]
        for i in range(nl):
            for j in range(nl):
                newarr[i][j] = matrix[x+nl+i][y+nl+j]
        is_same(newarr, x+nl, y+nl, nl)


import copy
bcnt = 0
wcnt = 0
paper = copy.deepcopy(matrix)
l = N

is_same(paper, 0, 0, l)

print(wcnt)
print(bcnt)