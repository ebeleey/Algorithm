n = input()

count = 0
num = 666

while(1):
    if '666' in str(num):
        count +=1
    if int(n) == count:
        break
    num += 1

print(num)
