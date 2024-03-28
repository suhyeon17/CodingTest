def solution(s):
    num = []
    s = s.split()
    
    for i in s:
        num.append(int(i))
            
    return str(min(num)) + ' ' + str(max(num))