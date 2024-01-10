def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    set1, set2 = {}, {}
    for i in range(len(str1)-1):
        st = str1[i:i+2]
        if st.isalpha():
            if st not in set1:
                set1[st] = 1
            else:
                set1[st] += 1
                
    for i in range(len(str2)-1):
        st = str2[i:i+2]
        if st.isalpha():
            if st not in set2:
                set2[st] = 1  
            else:
                set2[st] += 1
    
    set_inter, set_union = {}, {}
    for k, v in set1.items():
        if k in set2:
            set_inter[k] = min(set1[k], set2[k])
            
    for k, v in set1.items():
        if k in set2:
            set_union[k] = max(set1[k], set2[k])
        else:
            set_union[k] = v
    for k, v in set2.items():
        if k not in set_union:
            set_union[k] = v
            
    inter, union = 0, 0
    for k, v in set_union.items():
        union += v
    for k, v in set_inter.items():
        inter += v
        
    if union == 0:
        return 65536
    else:
        return int(inter/union * 65536) 
    