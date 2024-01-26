def solution(s):
    n = len(s)
    answer = []
    for i in range(1, n//2+1):
        zip_s = ''  
        idx = 0
        start, end = 0, 0+i
        while start < n: #조건은 나중에
            if end > n:
                zip_s += s[start:]
                break
            if s[start:start+i] == s[end:end+i]:
                end += i
            else:
                if (end-start)//i != 1:
                    zip_s += (str((end-start)//i) + s[start:start+i])
                    start = end
                    end += i
                else:
                    zip_s += s[start:start+i]
                    start = end
                    end += i
        answer.append(zip_s)
    
    if not answer:
        return len(s)
        
    answer.sort(key = lambda x:len(x))
    
    return len(answer[0])