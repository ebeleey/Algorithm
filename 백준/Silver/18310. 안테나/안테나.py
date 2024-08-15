N = int(input()) # 집의 수
houses = list(map(int, input().split())) # 집 위치

houses.sort()
print(houses[(N-1)//2])