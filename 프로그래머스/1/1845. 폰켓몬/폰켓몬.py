def solution(nums):
    arr = [nums[0]]
    n = len(nums)
    
    for num in nums:
        if num not in arr:
            arr.append(num)
    
    if len(arr) > n//2:
        return n//2
    else:
        return len(arr)