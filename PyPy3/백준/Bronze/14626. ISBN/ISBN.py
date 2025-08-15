
isbn = list(input())

ans = 10
loss = 0

for i in range(13):
    if isbn[i] == '*':
        loss = i
    else:
        isbn[i] = int(isbn[i])

for i in range(12):
    if i != loss:
        if i % 2:
            ans += 3 * isbn[i]
        else:
            ans += isbn[i]

check = isbn[12]

for x in range(10):
    w = 3 if loss % 2 else 1
    tmp = x * w + ans
    if (tmp + check) % 10 == 0:
        print(x)
