import numpy as np


def pseudorandomBinarySeqUsingUni(N):

    uniList = np.random.uniform(0, 1, N)
    res = []
    for i in range(0, N):
        if (uniList[i] < 0.5):
            res.append(0)
        else:
            res.append(1)
    return res

def pseudorandomBinarySeqUsingNorm(N):

    normList = np.random.normal(0, 1, N)
    result = []
    for i in range(0, N):
        if (normList[i] < 0):
            result.append(0)
        else:
            result.append(1)
    return result

randBinListUni = pseudorandomBinarySeqUsingUni(10**6)
randBinListNorm = pseudorandomBinarySeqUsingNorm(10**6)

print("10^6 pseudorandom binary numbers using variables from the uniform distribution:")
for i in randBinListUni:
    print(i)

print("10^6 pseudorandom binary numbers using variables from the normal distribution:")
for i in randBinListNorm:
    print(i)