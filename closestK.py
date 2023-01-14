from heapq import *
def findClosestElements(arr, k, x):
    heap = []
    for n in arr:
        dist = abs(n - x)
        t = (-dist, -n)

        heappush(heap, t)

        if len(heap) > k:
            heappop(heap)

    print(heap)
    res = []
    for _ in range(k):
        dist, num = heappop(heap)
        res.append(-num)

    print(sorted(res))
    return res
k = 4
x = 3
nums = [1,2,3,4,5]

findClosestElements(nums, k ,x)