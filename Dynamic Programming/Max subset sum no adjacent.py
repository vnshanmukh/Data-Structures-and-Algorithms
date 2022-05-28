def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    maxsum = array[:]
    maxsum[1] = max(array[0],array[1])
    for i in range(2,len(array)):
        maxsum[i] = max(maxsum[i-1],maxsum[i-2]+array[i])
    return maxsum[-1]