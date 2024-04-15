import heapq as hq

def solution(operations):
    h = []
    for op in operations:
        if op == 'D -1':
            if len(h) == 0:
                pass
            else:
                hq.heappop(h) 
        elif op == 'D 1':
            if len(h) == 0:
                pass
            else:
                h = hq.nlargest(len(h), h)[1:]
                hq.heapify(h)
                print(h)
        else:
            if op[2] == '-':
                num = int(op[3:]) * (-1)
                hq.heappush(h, num)
            else:
                num = int(op[2:])
                hq.heappush(h, num)
                
    if len(h) == 0:
        return [0, 0]
    else:
        return [max(h), h[0]]