from functools import reduce

def CountTriplets(a, ctr):

    def greedy(arr, ctr):
        if len(arr) < 3:
            return
        if reduce(lambda x,y: x*y, arr) % 2 == 0:
            print(arr)
            ctr += 1
            return

        for i in range(len(arr)):
            greedy([arr[i]] + arr[i+1:i+3], ctr)


    greedy(a, ctr)

# Driver code
if __name__ == "__main__":
    arr = [2,4,8,2]
    ctr = 0
    print(CountTriplets(arr, ctr))

# This code is contributed by Chitranayal
