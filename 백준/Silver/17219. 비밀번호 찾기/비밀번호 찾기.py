N, M = map(int, input().split()) # 저장된 사이트 주소의 수 N, 비밀번호 찾으려는 사이트 주소의 수 M

dict = {}

for _ in range(N):
    address, password = input().split()
    dict[address] = password

for _ in range(M): # 비밀번호를 찾으려는 사이트 주소
    print(dict[input()])
