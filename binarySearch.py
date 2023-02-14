def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    first = 0
    last = len(nums) - 1

    while first<=last:
        mid = first + ((last - first) // 2)
        if target < nums[mid]:
            last = mid - 1
        elif target > nums[mid]:
            first = mid+1
        else:
            return mid
    return -1

    


            

    
print(search([-1,0,3,5,9,12,13],9))
    