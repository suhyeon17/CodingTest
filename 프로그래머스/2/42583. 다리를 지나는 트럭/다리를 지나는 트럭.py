from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    sum_w = 0
    
    while bridge:
        time += 1
        sum_w -= bridge.pop()
        if truck_weights:
            if sum_w + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.appendleft(truck)
                sum_w += truck
            else:
                bridge.appendleft(0)
    
    return time