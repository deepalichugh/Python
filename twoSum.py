def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    arr = set()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums and nums.index(diff) != i:
            second_num = nums.index(diff)
            first_num = i
            break
    print(first_num, second_num)

twoSum([3,2,4],6)        