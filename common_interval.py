def minAvailableDuration(slots1, slots2, duration):
    i = j = 0
    res = []

    while i < len(slots1) and j < len(slots2):

        a_start, a_end = slots1[i]
        b_start, b_end = slots2[j]

        # check for overlap
        st = max(a_start, b_start)
        end = min(a_end, b_end)
        if end - st >= duration:
            res = [st, st+duration]
            break
        elif a_end < b_end:
            i += 1
        else:
            j += 1

    print(res)
    return res

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 11

minAvailableDuration(slots1, slots2, duration)
