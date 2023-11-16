def solution(s):
    cnt = 0
    re = 0
    while s != '1':
        answer = []
        before = len(s)
        s = s.replace('0', '')
        c = len(s)
        re += (before - c)
        while c > 0:
            answer.append(c%2)
            c //= 2

        s = ''.join(str(i) for i in answer[::-1])
        cnt += 1
        
    return [cnt, re]