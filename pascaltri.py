def pascaltriangle(n):
    j = 0
    res = [ [1] * (i+1)  for i in range(n+1) ]

    for i in range(2, n+1):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]

    for x in res:
        print(x)

n = 4
pascaltriangle(n)
