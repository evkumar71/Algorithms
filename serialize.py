from pickle import dump, load

def ser():
    fil = open("vijay.txt", "wb")

    L = [1,3,6,8, 99]

    dump(L, fil)
    fil.close()

    fil = open("vijay.txt", "rb")
    L2 = load(fil)
    print(L2)

ser()