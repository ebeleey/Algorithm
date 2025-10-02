string = input()
bomb = list(input())

B = len(bomb)
ans = []

for s in string:
    ans.append(s)
    if ans[-B:] == bomb:
        del ans[-B:]

print(''.join(ans) if ans else "FRULA")
