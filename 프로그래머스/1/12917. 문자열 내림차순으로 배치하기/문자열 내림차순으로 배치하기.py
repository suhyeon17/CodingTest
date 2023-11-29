def solution(s):
    arr = list(str(s))
    arr = sorted(arr, reverse = True)
    
    return ''.join(arr)