import heapq as hq
def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        hq.heappush(scoville, a+b*2)
        cnt += 1
    
    return cnt