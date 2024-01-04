def solution(s):
    answer = []
    
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key= lambda x:len(x))
    
    for i in range(len(s)):
        nn = s[i].split(',')
        for n in nn:
            if int(n) not in answer:
                answer.append(int(n))
                
    return answer
    
    
    