chars = input()

ans = 0
is_minus = False
temp = ''
temp_sum = 0

for char in chars:
    if char == '-':
        temp_sum += int(temp)
        if is_minus:
            ans -= temp_sum
        else:
            ans += temp_sum
            is_minus = True
        temp_sum = 0
        temp = ''
    elif char == '+':
        temp_sum += int(temp)
        temp = ''
    else:
        temp += char

temp_sum += int(temp)
if is_minus:
    ans -= temp_sum
else:
    ans += temp_sum

print(ans)