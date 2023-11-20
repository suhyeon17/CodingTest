def solution(s):
    stack = []
    
    for alpha in s:
        if not stack or alpha != stack[-1]:
            stack.append(alpha)
        elif alpha == stack[-1]:
            stack.pop()
            
    if not stack:
        return 1
    else:
        return 0
