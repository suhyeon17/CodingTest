def solution(s):
    bracket = []
    
    for b in s:
        if b == '(':
            bracket.append(b)
        else:
            if len(bracket) == 0:
                return False
            else:
                bracket.pop()
        
    if len(bracket) == 0:
        return True
    else:
        return False