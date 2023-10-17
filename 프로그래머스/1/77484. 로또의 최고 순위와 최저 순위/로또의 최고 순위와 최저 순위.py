def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    new_lottos = []
    cnt = 0
    
    for l in lottos:
        if l not in win_nums:
            new_lottos.append(l)
    for n in new_lottos:
        if n == 0:
            cnt += 1
    
    low, high = 6-len(new_lottos), 6-len(new_lottos)+cnt
    
    answer.append(rank[high])
    answer.append(rank[low])
    
    return answer