from scipy import stats

alpha = 0.05
M = 15
m = 2

def pseudorandom(x0, N):
    
    res = []
    res.append(x0)
    for i in range(1, N):
        x = res[i - 1] * ((M % pow(2, m)) / (pow(2, m)))
        res.append(x)
    return res

print(pseudorandom(1, 100))

stat, p = stats.kstest(pseudorandom(1, 100), "uniform")

print("p-value = {:g}".format(p))

if p < alpha:
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")