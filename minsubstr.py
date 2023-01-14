from collections import Counter

def minWindow(s, t):
    print(s)
    T = Counter(t)
    C = {}
    st = ctr = 0
    mn = float('inf')
    res = ""

    matched = 0
    for j in range(len(s)):
        # print(f"j= {j} {s[j]} -- {st} {s[st]}")
        if s[j] in T:
            if s[j] in C:
                C[s[j]] += 1
            else:
                C[s[j]] = 1

        # print(f"{C}  {s[st:j+1]}")

        # all found
        if  C == T:
            if len(s[st:j + 1]) < mn:
                res = s[st:j + 1]
                mn = len(res)

            print(f"Min {mn}  {C} {res}")

            # char to be removed
            while st <= j and s[st] in T:
                if C[s[st]] > 0:
                    C[s[st]] -= 1
                st += 1

    return res

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))