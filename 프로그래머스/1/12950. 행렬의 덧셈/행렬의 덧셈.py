def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr1[0])
    answer = []

    for i in range(r): 
        arr = []
        for j in range(c):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    
    return answer