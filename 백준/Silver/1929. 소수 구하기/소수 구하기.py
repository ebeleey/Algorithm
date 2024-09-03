#소수 구하기

M, N = map(int, input().split()) # M이상 N이하의 소수를 모두 출력

arr = [True] * (N+1)
arr[0] = False
arr[1] = False

for i in range(2, N+1):
    if arr[i] == True:
        k = 2
        while (i*k) <= N:
            arr[i*k] = False #i의 배수 값을 지워준다.
            k += 1

for i in range(M, len(arr)):
    if arr[i] == True:
        print(i)