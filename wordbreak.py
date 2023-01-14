def wordbreak(s):
    st = 0
    res = True
    while st < len(s) and res:
        res = False
        for w in wordDict:
            en = len(w)
            print(s[st:st+en])
            if s[st:st+en] == w:
                st += en
                found = True
                break

    return res

wordDict = ["leet","code"]
s = 'leetcode'
res = wordbreak(s)
print(res)