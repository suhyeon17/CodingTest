def solution(n, m, section):
    cnt = 0
    
    while len(section) != 0:
        paint = section[0] + m - 1 
        cnt += 1
        
        for i in range(len(section)):
            if section[0] <= paint:
                section.pop(0)
            else:
                break
            
    return cnt