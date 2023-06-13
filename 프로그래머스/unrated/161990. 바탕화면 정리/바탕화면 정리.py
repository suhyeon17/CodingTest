def solution(wallpaper):
    n_row = len(wallpaper)
    n_col = len(wallpaper[0])
    #결과값 초기화
    lux, luy, rux, ruy = n_row, n_col, 0, 0
    
    for i in range(n_row):
        for j in range(n_col):
            if wallpaper[i][j] == '#':
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rux < i:
                    rux = i
                if ruy < j:
                    ruy = j
    
    return [lux, luy, rux + 1, ruy + 1]
    