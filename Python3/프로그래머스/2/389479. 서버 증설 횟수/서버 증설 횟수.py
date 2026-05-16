def solution(players, m, k):
    answer = 0
    
    exp_servers = [0] * 24 # 각 시간 별로 반납될 서버 수
    pres_server = 0 # 현재 운영중인 서버 수
    
    for i in range(24):
        pres_server -= exp_servers[i] # 서버 반납
        
        need = max(0, players[i] // m - pres_server) # 증설이 필요한 서버 수
        
        answer += need # 증설 횟수 업데이트
        pres_server += need # 현재 운영중인 서버 수 업데이트
        
        if i + k < 24:
            exp_servers[i + k] += need # 반납 리스트 업데이트
            
    return answer