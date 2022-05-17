def solution(nums):
    size = int(len(nums) / 2)
    nums = set(nums)
    
    if size > len(nums):
        return len(nums)
    else:
        return size