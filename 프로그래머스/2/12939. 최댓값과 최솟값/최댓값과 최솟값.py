def solution(s):
    num = []
    s = s.split(' ')
    
    for n in s:
        num.append(int(n))
        
    return '%d %d' %(min(num), max(num))