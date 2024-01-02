from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                people.pop()
                people.popleft()
            else:
                people.pop()
        else:
            people.pop()
        
        cnt += 1
        
    return cnt