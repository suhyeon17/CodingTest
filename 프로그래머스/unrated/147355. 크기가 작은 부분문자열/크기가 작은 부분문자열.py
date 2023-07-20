def solution(t, p):
    answer = 0
    l = len(p)
    i = 0
    
    while i + l <= len(t):
        if int(t[i:i+l]) <= int(p):
            answer += 1
        i += 1
        
    return answer