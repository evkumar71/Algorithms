def uniqsubstr(s, k):
    print(s)
    if k > len(s):
        return 0

    st, ctr = 0, 0
    dic = {}

    for i in range(len(s)):
        while s[i] in dic:
            # print(f"Now {i} {s[i]} {s[st]} {dic}")
            del dic[s[st]]
            st += 1

        dic[s[i]] = 1

        if len(dic) > k:
            del dic[s[st]]
            st += 1

        if len(dic) == k:
            print(''.join(dic.keys()))
            ctr += 1

    return ctr

s = 'havefunonleetcode'
k = 5
print(uniqsubstr(s,k))