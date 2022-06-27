class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftsum =0 
        for i,x in enumerate(nums):
            if leftsum == (s-x-leftsum):
                return i
            leftsum +=x
        return -1