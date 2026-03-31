def solution(n, words):
    
    word_set = set()
    num = 0
    
    while num < len(words):
        if (len(words[num]) == 1) or (words[num] in word_set) or ((num >= 1) and (words[num - 1][-1] != words[num][0])):
            answer = [num % n + 1, num // n + 1]
            break
        else :
            word_set.add(words[num])
            num += 1
    else: 
        answer = [0, 0]
        
    return answer