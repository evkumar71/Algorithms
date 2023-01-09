def bubsort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


n = [2,0,2,1,1,0]
print(n)
bubsort(n)
print(n)