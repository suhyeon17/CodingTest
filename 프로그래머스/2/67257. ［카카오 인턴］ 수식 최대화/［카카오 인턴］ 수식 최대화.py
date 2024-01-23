import re
from itertools import permutations
def cal(num1, num2, op):
    if op == '*':
        return num1*num2
    elif op == '-':
        return num1-num2
    else:
        return num1+num2

def solution(expression):
    answer = []
    op = set(re.findall(r'[\+,\-,\*]', expression))
    n = len(op)
    
    for p in permutations(op, n):
        operand = list(map(int, re.split(r'[\+,\-,\*]', expression)))
        operate = [e for e in expression if e in '+-*']
        for i in range(n):
            while p[i] in operate:
                idx = operate.index(p[i])
                num = cal(operand[idx], operand[idx+1], operate[idx])
                operand[idx] = num
                operand.pop(idx+1)
                operate.pop(idx)
        answer.append(abs(operand[0]))

    return max(answer)
                    
                    