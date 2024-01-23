def check(blank):
    stack = []
    for b in blank:
        if b == '(':
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else: return False
    if stack:
        return False
    
    return True

def solution(p):
    #1
    if not p:
        return p
    #2
    o, c = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            o += 1
        else:
            c += 1
            
        if o == c:
            break
    u = p[:i+1]
    v = p[i+1:]
    
    
    #3
    if check(u):
        return u + solution(v)
    
    #4
    else:
        new_v = '('
        new_v += solution(v)
        new_v += ')'
        new_u = ''
        
        for i in range(1, len(u)-1):
            if u[i] == '(':
                new_u += ')'
            else:
                new_u += '('
        return new_v + new_u
    
    