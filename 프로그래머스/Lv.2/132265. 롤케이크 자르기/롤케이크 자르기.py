from collections import Counter

def solution(topping):
    cnt = 0
    chulsu = Counter(topping)
    brother = set()
    
    for t in topping:
        chulsu[t] -= 1
        brother.add(t)
        
        if chulsu[t] == 0:
            chulsu.pop(t)
        if len(chulsu) == len(brother):
            cnt += 1
    
    return cnt