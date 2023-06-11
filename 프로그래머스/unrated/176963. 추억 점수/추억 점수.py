def solution(name, yearning, photo):
    answer = []
    memory = dict()
    
    for i in range(len(name)):
        memory[name[i]] = yearning[i]

    for i in photo:
        memory_sum = 0
        for j in i:
            if j in name:
                memory_sum += memory[j]

        answer.append(memory_sum)	
        
    return answer