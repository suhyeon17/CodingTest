def solution(n, lost, reserve):
    lost_num = len(lost)
    
    #여벌이 있는 학생이 도난 당했을 경우
    #돌면서 지우니까 리스트가 망가져서 제대로 loop를 돌지 않음
    for l in range(1,n+1):
        if l in lost and l in reserve:
    
            lost_num -= 1
            reserve.remove(l)
            lost.remove(l)
            
    lost.sort()

    #그 외
    for l in lost:
        if l-1 in reserve:
            lost_num -= 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            lost_num -= 1
            reserve.remove(l+1)
        else:
            pass
            
    return n-lost_num