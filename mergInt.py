def mergintr(intervals, newInterval):
    print(f"orig {intervals} <---> {newInterval}")

    idx = 0
    res = []

    # new starting after cur-ends
    while idx < len(intervals):
        prev = intervals[idx]
        if newInterval[0] <= prev[1]:
            break
        else:
            res.append(prev)
            idx += 1

    res.append(newInterval)

    for cur in intervals[idx:]:
        cur_st, cur_end = cur[0], cur[1]
        prev = res[-1]
        prev_st, prev_end = prev[0], prev[1]

        if cur_st <= prev_end:
            st = min(prev_st, cur_st)
            end = max(prev_end, cur_end)
            res[-1] = [st, end]
        else:
            res.append(cur)

    print(f"final {res}")
    return res

intr = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_intr = [4,8]

mergintr(intr, new_intr)