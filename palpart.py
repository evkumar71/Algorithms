def palpart(s):

    def back(s, start, path=[]):
        #print(f"Len: {len(s[start:])} : {s[start:]}")
        if start >= len(s):
            res.append(path)
            return

        for end in range(start, len(s)):
            temp = s[start:end+1]
            # print(f"{start}: {temp}")
            if temp == temp[::-1]:
                #print(f"Pal: {temp} from {start} for {s[start:]}")
                back(s, end+1, path + [temp])

    res = []
    back(s, 0)
    print(f"Res: {res}")

s = 'aabab'
print(f"orig: {s}")
palpart(s)