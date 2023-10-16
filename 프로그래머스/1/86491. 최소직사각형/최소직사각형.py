def solution(sizes):
    max_r, max_c = 0,0
    
    for size in sizes:
        if size[0] < size[1]:
            r_idx, c_idx = 1, 0
        else:
            r_idx, c_idx = 0, 1
        
        if max_r < size[r_idx]: max_r = size[r_idx]
        if max_c < size[c_idx]: max_c = size[c_idx]
        
    return max_r * max_c