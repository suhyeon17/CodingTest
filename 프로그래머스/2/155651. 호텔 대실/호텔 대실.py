import heapq

def tTom(i, o):
    i = int(i[:2])*60 + int(i[3:])
    o = int(o[:2])*60 + int(o[3:]) + 10
    
    return i, o

def solution(book_time):
    book_time.sort()
    rooms = []
    for time in book_time:
        i, o = tTom(time[0], time[1])
        if rooms and rooms[0] <= i:
            heapq.heappop(rooms)    
        heapq.heappush(rooms, o)
        
    return len(rooms)
        