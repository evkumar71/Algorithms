def stkop(s, res):
    if not stk:
        return

    for i in range(len(s)):
        if s[i] == '[':
            stkop(s[i+1:], res)
        elif s[i] == ']':
            return
        else:
            res += [s[i]]

if __name__ == '__main__':
    s = "2[a]3[bc]"
    res = []
    stkop(s, 0,  res)