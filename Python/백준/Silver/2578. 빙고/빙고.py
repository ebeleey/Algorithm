N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]
speak = [list(map(int, input().split())) for _ in range(N)]


row_bingo = [False] * N
col_bingo = [False] * N
dia_bingo_1 = False
dia_bingo_2 = False

row_bingo_count = [0] * N
col_bingo_count = [0] * N
dia_bingo_1_count = 0
dia_bingo_2_count = 0

def bingo_check():
    global count
    global dia_bingo_1_count, dia_bingo_2_count, dia_bingo_1, dia_bingo_2
    for i in range(N):
        if not row_bingo[i] and row_bingo_count[i] == 5:
            row_bingo[i] = True
            count += 1
        if not col_bingo[i] and col_bingo_count[i] == 5:
            col_bingo[i] = True
            count += 1
    if not dia_bingo_1 and dia_bingo_1_count == 5:
        dia_bingo_1 = True
        count += 1
    if not dia_bingo_2 and dia_bingo_2_count == 5:
        dia_bingo_2 = True
        count += 1

    if count >= 3:
        return True
    return False

def erase(num):
    global dia_bingo_1_count, dia_bingo_2_count
    for i in range(N):
        for j in range(N):
            if bingo[i][j] == num:
                row_bingo_count[i] += 1
                col_bingo_count[j] += 1
                if i == j:
                    dia_bingo_1_count += 1
                if j == (N -1- i):
                    dia_bingo_2_count += 1
                return


idx = 0
count = 0
flag = False
for row in speak:
    for num in row:
        idx += 1
        erase(num)
        
        if bingo_check():
            print(idx)
            flag = True
            break
    if flag:
        break
    
        


