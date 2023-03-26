def genpar(n):
    stk = [('', n, n)]
    l = r = n
    res = []
    while stk:
        st, l, r = stk.pop()

        if l == r == 0:
            res += [st]

        if l > 0:
            stk.append((st + '(', l - 1, r))

        if r > l:
            stk.append((st + ')', l, r - 1))

    return res

n = 3   # number of "pairs of left and right paren"
res = genpar(n)
print(res)