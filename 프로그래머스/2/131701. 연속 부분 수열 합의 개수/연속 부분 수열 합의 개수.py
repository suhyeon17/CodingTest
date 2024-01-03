from collections import deque
import itertools

def solution(elements):
    answer = []
    elements = deque(elements)
    
    for i in range(1, len(elements)+1):
        for _ in range(len(elements)):
            answer.append(sum(itertools.islice(elements, 0, i)))
            front = elements.popleft()
            elements.append(front)

    return len(set(answer))