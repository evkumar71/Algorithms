def isPalindrome(x: int):
    s = str(x)
    i = j = 0
    L = len(s)-1

    if len(s) % 2 != 0:
        i = (L // 2) - 1
        j = (L // 2) + 1
    else:
        i = L // 2
        j = (L // 2) + 1

    while i >= 0 and j < len(s):
        if s[i] != s[j]:
            return False

        i -= 1
        j += 1

    return True

n = 898
print(isPalindrome(n))