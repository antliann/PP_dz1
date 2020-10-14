import numpy as np
from matplotlib import pyplot as plt


def maxUniList(N, n):

    res = []
    for i in range(0, N):
        uniList = np.random.uniform(0, 1, n)
        res.append(max(uniList))
    return res

maxUniListSample = maxUniList(2000, 100)
for i in maxUniListSample:
    print(i)

plt.xlim([min(maxUniListSample)-0.01, 1])
plt.hist(maxUniListSample, bins=100, alpha=1)
plt.title('MaxUniform(0,1) histogram')
plt.xlabel('MaxUniform(0,1) variable')
plt.ylabel('count')

plt.show()