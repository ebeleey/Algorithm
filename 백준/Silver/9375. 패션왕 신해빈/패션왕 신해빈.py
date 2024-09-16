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

    result = 1
    for item in lst:
        result *= item + 1

    print(result - 1)
