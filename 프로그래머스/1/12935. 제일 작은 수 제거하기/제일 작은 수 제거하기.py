def solution(arr):
    n = min(arr)
    arr.remove(n)
    
    if not arr:
        return [-1]
    
    return arr