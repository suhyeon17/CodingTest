def solution(park, routes):
    n_row = len(park)
    n_col = len(park[0])
    
    #시작, 장애물 위치 찾기 -> park는 일차원 리스트~,~
    blocks = []
    for i in range(n_row):
        for j in range(n_col):
            if park[i][j] == 'S':
                now_row, now_col = i, j
            elif park[i][j] == 'X':
                blocks.append([i, j])
            else:
                pass
    
    #강아지 명령어 수행
    for route in routes:
        op, move = route.split()
        move = int(move)
        n_block = len(blocks)
        meet = False
        
        if op == 'N':
            tmp = now_row - move
            #park에 벗어나는지 확인
            if tmp >= 0 and tmp < n_row:
                #장애물 만나는지 확인
                if n_block > 0:
                    for b in blocks:
                        if now_col == b[1] and now_row >= b[0] and tmp <= b[0]:
                            meet = True
                            break
                if not meet:
                    now_row = tmp
                
        elif op == 'S':
            tmp = now_row + move
            #park에 벗어나는지 확인
            if tmp >= 0 and tmp < n_row:
                #장애물 만나는지 확인
                if n_block > 0:
                    for b in blocks:
                        if now_col == b[1] and now_row <= b[0] and tmp >= b[0]:
                            meet = True
                            break
                if not meet:
                    now_row = tmp

        elif op == 'W':
            tmp = now_col - move
            #park에 벗어나는지 확인
            if tmp >= 0 and tmp < n_col:
                #장애물 만나는지 확인
                if n_block > 0:
                    for b in blocks:
                        if now_row == b[0] and now_col >= b[1] and tmp <= b[1]:
                            meet = True
                            break
                if not meet:
                    now_col = tmp
        else:
            tmp = now_col + move
            #park에 벗어나는지 확인
            if tmp >= 0 and tmp < n_col:
                #장애물 만나는지 확인
                if n_block > 0:
                    for b in blocks:
                        if now_row == b[0] and now_col <= b[1] and tmp >= b[1]:
                            meet = True
                            break
                if not meet:
                    now_col = tmp
                    
    return [now_row, now_col]