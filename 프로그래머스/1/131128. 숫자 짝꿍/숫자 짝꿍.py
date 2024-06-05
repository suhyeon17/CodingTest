#1. X, Y에 있는 숫자 0~9까지 개수 세기
#2. for i in range(10):
#3.     if x_dict[i]>0 and y_dict[i]>0:
#4.     min(x_dict[i], y_dict[i])*i 만큼 담기

def solution(X, Y):
    answer = ''
    x_dict, y_dict = {}, {}
    for i in range(10):
        x_dict[i] = X.count(str(i))
        y_dict[i] = Y.count(str(i))
        
    for i in range(9, -1, -1):
        if x_dict[i] > 0 and y_dict[i] > 0:
            answer += (str(i) * min(x_dict[i], y_dict[i]))
            
    if len(answer) == 0:
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
    
    print(answer)
    
    
 