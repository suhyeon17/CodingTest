def solution(id_list, report, k):
    id_dict, get_dict, valid_set = {}, {}, set()
    
    for id in id_list:
        id_dict[id] = 0
        get_dict[id] = 0
        
    for r in report:
        if r not in valid_set:
            valid_set.add(r)
            get = r.split()[1]
            get_dict[get] += 1
    
    k_list = []
    for id in id_list:
        if get_dict[id] >= k:
            k_list.append(id)

    for valid in valid_set:
        if valid.split()[1] in k_list:
            id_dict[valid.split()[0]] += 1
            
    return list(id_dict.values())
