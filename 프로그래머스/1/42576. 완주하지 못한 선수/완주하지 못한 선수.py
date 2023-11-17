def solution(participant, completion):
    p_dict = {}
    
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
            
    for c in completion:
        if p_dict[c] > 0:
            p_dict[c] -= 1
        
    for p in participant:
        if p_dict[p] > 0:
            return p
