def solution(X, Y):
    answer = ''
    dictX = {}
    dictY = {}
    
    for i in range(10):
        dictX[i] = X.count(str(i))
        dictY[i] = Y.count(str(i))
    
    for i in range(10):
        if dictX[i] > 0 and dictY[i] > 0:
            answer += str(i) * min(dictX[i], dictY[i])
    
    answer = ''.join(sorted(answer, reverse = True))
    
    if len(answer) == 0:
        return '-1'
    elif answer.count('0') == len(answer):
        return '0'
    else:
        return answer