def ksubarray(s, k):
    dic = {}
    ctr = wstart = 0

    for wend in range(len(s)):
        ch = s[wend]

        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

        if wend >= k-1:
            if len(dic) == k:
                ctr +=1
                print(''.join(dic))

            c = s[wstart]

            if dic[c] == 1:
                del dic[c]
            else:
                dic[c] -= 1

            wstart += 1

    return ctr

s = "havefunonleetcode"
k = 5
print(f"Str --> {s}")
res = ksubarray(s, k)
print(res)