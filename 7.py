import numpy as np


def randomBinarySeq(N):

    normList = np.random.normal(0, 1, N + 1)
    res = []
    for i in range(0, N):
        if (normList[i + 1] - normList[i] > 0):
            res.append(1)
        else:
            res.append(0)
    return res


randBinList = randomBinarySeq(1000)
count0 = 0
for i in randBinList:
    print(i)
    if (i == 0):
        count0 += 1

print("The empirical distribution function is:")
print("F(x) = 0 for x<0")
print("{0} for 0<=x<1".format((count0 / len(randBinList))))
print("1 for x>=1")
