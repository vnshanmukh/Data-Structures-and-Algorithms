class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = {}
        for i in arr:
            c[i] = c.get(i,0)+1
        try:
            if c[0] > 1:
                return True
        except KeyError:
            pass
        S = set(arr) - {0}
        for i in arr:
            if 2*i in S:
                return True
        return False