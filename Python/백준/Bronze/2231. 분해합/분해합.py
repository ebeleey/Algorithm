n =int(input())

def sum_of_digits(numbers): #문자열이 들어옴
    digitsum = 0
    for num in numbers:
         digitsum += int(num)
    return digitsum
    
flag = False

for m in range(1, n+1):
    digitsum = sum_of_digits(str(m))
    if (m + digitsum == n):
        print(m)
        flag = True
        break

if flag== False:
    print(0)

