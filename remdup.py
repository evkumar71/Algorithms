def removeDuplicates(nums):

    st = 0
    en = 1

    while en < len(nums):
        if nums[st] == nums[en]:
            en += 1
            continue

        nums[st + 1] = nums[en]
        st += 1
        print(nums)
    return st

n = [0,0,1,1,1,1,1,2,2,3]
res = removeDuplicates(n)
print(n[:res+1])