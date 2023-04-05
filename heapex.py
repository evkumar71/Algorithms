from heapq import heappush, heappop

def heapex(nums) -> int:
    h = []

    for n in nums:
        heappush(h, n)

    mx = ctr = 0
    prev = None

    while h:
        num = heappop(h)

        print(f"{ctr} --> {num}")

        if not prev:
            ctr = 1
        elif num == prev + 1:
            ctr += 1
        else:
            ctr = 1

        prev = num
        #print(f"max = {mx}")
        mx = max(mx, ctr)

n = [0,3,7,2,5,8,4,6,0,1]
heapex(n)