def change(amount, coins):

    def back(amt, coins, ctr):
        if amt == 0:
            ctr[-1] += 1
            return
        if amt < 0:
            return

        for i in range(len(coins)):
            back(amt - coins[i], coins, ctr)

    ctr = [0]
    back(amount, coins, ctr)
    return ctr[-1]

n = 5
coins = [1,2,5]
res = change(n, coins)
print(res)