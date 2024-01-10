from itertools import permutations

def solution(k, dungeons):
    m = len(dungeons)
    tmp = k #원래 k 저장
    answer = []
    
    for dungeon in permutations(dungeons, m):
        k = tmp
        cnt = 0
        
        #각 순열마다 확인
        for d in dungeon:
            if d[0] <= k: #최소 필요 피로도가 충족
                k -= d[1]
                cnt += 1
            else: break
        answer. append(cnt)
            
    return max(answer)