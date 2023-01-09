def cyclicsort(nums):

    i = 0
    while i < len(nums):
        print(nums)
        idx = nums[i]   # number to be in that idx-position

        if nums[i] < len(nums)  and i != nums[i]:
            nums[idx], nums[i] = nums[i], nums[idx]
            print(f"Moverd: {nums}")
        else:
            i += 1

n = [3,0,1]
cyclicsort(n)
