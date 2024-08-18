import sys

N, K = map(int, sys.stdin.readline().split()) # 온도를 측정한 전체 날짜의 수 N , 합을 구하기 위한 연속적인 날짜의 수 K

temps = list(map(int, sys.stdin.readline().split()))
# temp_sum = [0] * (N+1-K)
#
# for i in range(len(temp_sum)):
#     for k in range(K):
#         temp_sum[i] += temps[i+k]
#
# print(max(temp_sum))

cursum = sum(temps[:K]) # 초기 K일 합
maxsum = cursum

for i in range(K, N):
    cursum += temps[i] - temps[i-K]
    if maxsum < cursum:
        maxsum = cursum
print(maxsum)
