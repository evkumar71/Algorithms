def isValid(st):
    cnt = 0
    for x in st:
        if x == '(': cnt += 1
        elif x == ')': cnt -= 1
        if cnt < 0:
            return False

    return cnt == 0

st = '((()))()()()'
st = ')'
print(isValid(st))