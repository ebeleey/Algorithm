def solution(k, tangerine):
    answer = 0
    
    cnt = [0]* (max(tangerine) + 1)
    
    for i in range(len(tangerine)):
        cnt[tangerine[i]] += 1
        
    
    cnt.sort(reverse = True)
    
    tmp = k
    
    for x in cnt:
        tmp -= x
        answer += 1        
        if tmp <= 0:
            break
            
    
    
    return answer
