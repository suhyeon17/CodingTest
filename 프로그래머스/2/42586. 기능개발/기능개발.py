import math
from collections import deque

def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(speeds)):
        n = math.ceil((100-progresses[i]) / speeds[i])
        days.append(n)

    days = deque(days)
    now = days.popleft()
    cnt = 1
    
    while days:
        next = days.popleft()
        
        if now < next:
            answer.append(cnt)
            cnt = 1
            now = next
        else:
            cnt += 1
            
    answer.append(cnt)
    return answer