from itertools import product
def solution(numbers, target):
    cnt = 0
    buho = []
    for p in product(['+', '-'], repeat = len(numbers)):
        buho.append(p)
    
    for b in buho: 
        num = 0
        for i in range(len(numbers)):
            if b[i] == '+':
                num += numbers[i]
            else:
                num -= numbers[i]
        if num == target:
            cnt += 1

    return cnt
        
        