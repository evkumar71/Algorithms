
def bsearch(lo, hi, num):

    # res = False
    # while lo <= hi:
    #     mid = (lo + hi) // 2
    #
    #     if num == ar[mid]:
    #         res = True
    #         break
    #     elif num < ar[mid]:
    #         hi = mid - 1
    #     else:
    #         lo = mid + 1
    #
    # return res

    if lo <= hi:
        mid = (lo + hi) // 2

        if num == ar[mid]:
            return True
        elif num < ar[mid]:
            return bsearch(lo, mid-1, num)
        else:
            return bsearch(mid+1, hi, num)
    else:
        return False


ar = sorted([6,4,10,1,5,7,16])
num = 16

res = bsearch(0, len(ar)-1, num)
print(res)
