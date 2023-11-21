def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a_arr = bin(a)[2:].zfill(n)
        b_arr = bin(b)[2:].zfill(n)
        
        arr = ''
        for i in range(n):
            if a_arr[i] == '1' or b_arr[i] == '1':
                arr += '#'
            elif a_arr[i] == '0' and b_arr[i] == '0':
                arr += ' '
                
        answer.append(arr)
        
    return answer