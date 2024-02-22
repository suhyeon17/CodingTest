def solution(players, callings):
    player = {p:idx+1 for idx, p in enumerate(players)} 
    rank = {idx+1:p for idx, p in enumerate(players)}
    
    for call in callings:
        now = player[call] #현재순위
        before = rank[now-1] #내 앞사람
        player[call] -= 1 #나는 앞지름
        player[before] += 1 #내 앞사람은 뒤로
        rank[now] = before 
        rank[now-1] = call

    answer = []
    for k, v in rank.items():
        answer.append(v)
        
    return answer