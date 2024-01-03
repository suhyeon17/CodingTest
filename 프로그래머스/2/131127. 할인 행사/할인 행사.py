from collections import Counter
def solution(want, number, discount):
    answer = 0
    w_dict = {}
    for i in range(len(want)):
        w_dict[want[i]] = number[i]

    for i in range(len(discount)-9):
        d = discount[i:i+10]
        if w_dict == Counter(d):
            answer += 1
            
    return answer
        