W, H = map(int, input().split()) #가로 세로
N = int(input()) #상점의 개수

markets = [list(map(int, input().split())) for _ in range(N)]
DG_dir, DG_dis = map(int, input().split()) #동근이 방향, 거리

answer = 0

dong_pos = 0
if DG_dir == 1: #북쪽이면
    dong_pos = DG_dis
elif DG_dir == 2: #남쪽이면
    dong_pos = 2*W + H -DG_dis
elif DG_dir == 3: #서쪽이면
    dong_pos = 2*W + 2*H -DG_dis
else: #동쪽이면
    dong_pos = W+DG_dis


# 상점은
for m_dir, m_dis in markets:
    if m_dir == 1:  # 북쪽이면
        m_pos = m_dis
    elif m_dir == 2:  # 남쪽이면
        m_pos =2 * W + H - m_dis
    elif m_dir == 3:  # 서쪽이면
        m_pos = 2 * W + 2 * H - m_dis
    else:  # 동쪽이면
        m_pos = W + m_dis
    distance = min(abs(dong_pos - m_pos), 2*W + 2*H - abs(dong_pos - m_pos))
    # print(distance)
    answer += distance
print(answer)

