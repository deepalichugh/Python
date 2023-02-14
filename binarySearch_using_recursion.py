def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    first = 0
    last = len(nums) - 1

    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0

    while first<=last:
        mid = first + ((last - first) // 2)
        if target < nums[mid]:
            last = mid
            search(nums[:last], target)
        elif target > nums[mid]:
            first = mid+1
            search(nums[first:],target)
        else:
            return mid
    return -1

    


            

    
print(search([-1,0,3,5,9,12,13],3))
    