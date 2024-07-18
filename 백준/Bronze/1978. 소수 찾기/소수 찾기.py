
n = int(input())

numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    is_decimal = True

    if (num == 1):
        continue
    else:
        for x in range(2, num):
            if(num%x==0):
                is_decimal = False            
                break
        if(is_decimal == True):
            count+=1

print(count)