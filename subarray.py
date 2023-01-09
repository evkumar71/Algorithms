def subarray(nums):
    print(nums)
    mx = nums[0]
    cursum = nums[0]
    st = end = 0
    for i in range(1, len(nums)):
        if cursum + nums[i] > nums[i]:
            cursum += nums[i]       #  new element included in subarry
        else:
            cursum = nums[i]
            st = end = i  # start over a new subarray

        if cursum > mx:
            end = i
            mx = cursum

    print(f"max: nums[{st}:{end}] = {mx}")

#n = [5,4,-1,7,8]
n = [-2,1,-3,4,-1,2,1,-5,4]

subarray(n)