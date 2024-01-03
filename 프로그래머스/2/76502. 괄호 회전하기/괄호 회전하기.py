def solution(s):
    answer = 0
    ss = s*2
    stack = []
    
    for i in range(len(s)):
        check = ss[i:i+len(s)]
        cnt = 0
        #올바른 괄호 맞는지 체크
        for c in check:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    break
                a = stack.pop()
                if not ((c == ')' and a == '(') or (c == '}' and a == '{') or (c == ']' and a == '[')):
                    break
            cnt += 1
        #break없이 괄호 체크 for문 다 돌았으면 점수 올리기
        if cnt == len(s) and not stack:
            answer += 1 
    
    return answer