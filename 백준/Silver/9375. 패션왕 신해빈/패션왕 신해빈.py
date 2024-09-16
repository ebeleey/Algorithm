T = int(input())

for _ in range(T):
    n = int(input()) # 해빈이가 가진 의상의 수 n
    dict = {}

    for _ in range(n):
        name, type = input().split()
        if type in dict:
            dict[type] = dict[type] + 1
        else:
            dict[type] = 1

    lst = list(dict.values())

    if n > 0:
        result = lst[0] + 1
        for i in range(1, len(lst)):
            result = result * (lst[i] + 1)

        print(result - 1)
    else:
        print(0)