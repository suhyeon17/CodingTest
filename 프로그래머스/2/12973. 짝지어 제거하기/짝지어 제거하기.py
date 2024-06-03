#이중안됨, 뒤에서부터 제거?, 짝짓는거니까 stack?
#0. stack에 하나 담기
#1. for alpha in s:
#2.     stack[-1] == alpha면
#3.          stack.pop()
def solution(s):
    stack = []
    for alpha in s:
        if not stack or stack[-1] != alpha: #스택이 비거나 같지 않으면
            stack.append(alpha)
        else: #비지 않고 같으면
            stack.pop() 
    
    
    if not stack:
        return 1
    else: return 0
        