def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i, j = cmd[0], cmd[1]
        split = array[i-1:j]
        split.sort()
        answer.append(split[(cmd[2]-1)])
        
    return answer