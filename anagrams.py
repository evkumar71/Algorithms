from collections import Counter

def anagrams(s, p):
    dic1 = Counter(p)
    dic2 = {}
    k = len(p)
    res = []
    wstart = 0

    for i in range(len(s)):
        if s[i] in dic2:
            dic2[s[i]] += 1
        else:
            dic2[s[i]] = 1

        if i >= k-1:
            if dic1 == dic2:
                res.append(wstart)
                print(dic2)

            if dic2[s[wstart]] == 1:
                del dic2[s[wstart]]
            else:
                dic2[s[wstart]] -= 1

            wstart += 1

    return res

s = "dkddjldlotc"
p = "tco"

print(anagrams(s, p))