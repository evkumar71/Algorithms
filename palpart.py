def palpart(s):

    def back(s, start):
        #print(f"Len: {len(s[start:])} : {s[start:]}")
        if start >= len(s):
            return

        for end in range(start, len(s)):
            temp = s[start:end+1]
            # print(f"{start}: {temp}")
            if temp == temp[::-1]:
                print(f"Pal: {temp} from {start} for {s[start:]}")
            back(s, end+1)

    back(s, 0)

s = 'aab'
palpart(s)