def solution(s):
    p_num, y_num = 0, 0
    
    for a in s:
        if a == 'p' or a == 'P':
            p_num += 1
        elif a == 'y' or a == 'Y':
            y_num += 1
        else:
            pass
    
    if p_num != y_num:
        return False
    else:
        return True