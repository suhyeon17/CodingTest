def solution(s):
    answer = 0
    now = 0
    idx1 = 0
    idx2 = 0
    
    for alpha in s:
        if s[now] == alpha:
            idx1 += 1
        else:
            idx2 +=1
        
        if idx1 == idx2:
            answer += 1
            now += idx1+idx2
            idx1, idx2 = 0, 0
    
    if idx1 != idx2:
        answer += 1
            
    return answer