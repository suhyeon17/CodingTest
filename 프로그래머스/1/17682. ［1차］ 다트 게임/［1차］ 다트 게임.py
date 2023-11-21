def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    idx, rst, score = 0, [], ''

    for r in dartResult:
        if r.isdigit():
            score += r
            idx += 1
        elif r in bonus:
            score = int(int(score) ** bonus[r])
            rst.append(score)
            score = ''
        else:
            if r == '*':
                if len(rst) == 1:
                    rst[idx-1] = rst[idx-1]*2
                else:
                    rst[idx-2] = rst[idx-2]*2
                    rst[idx-1] = rst[idx-1]*2
            else:
                rst[idx-1] = rst[idx-1]*(-1)
    
    print(rst)            
    return sum(rst)
                    
                    