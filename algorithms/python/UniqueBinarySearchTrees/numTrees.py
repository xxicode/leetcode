def numTrees(self, n):
    if n == 1: return 1
    res = [1, 1]
    for i in range(2, n + 1):
        val = sum(res[j] * res[i - j - 1] for j in range(i))
        res.append(val)
    return res[n]