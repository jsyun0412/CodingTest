def solution(nums):
    n = set(nums)
    s = len(nums)//2
    
    if s < len(n):
        return s
    else:
        return len(n)
    