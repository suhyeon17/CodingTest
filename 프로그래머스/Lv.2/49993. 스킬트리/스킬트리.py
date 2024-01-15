from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    
    for tree in skill_trees:
        x = deque()
        for t in tree:
            if t in skill:
                x.append(t)
        
        i = 0
        check = True
        while x:
            if skill[i] != x.popleft():
                check = False
                break
            i += 1
            
        if not x and check:
            cnt += 1
            
    return cnt