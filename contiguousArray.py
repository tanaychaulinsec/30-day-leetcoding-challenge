class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums=[x if x else -1 for x in nums]
        prefixSum={0:-1}
        presum=res=0
        for i,x in enumerate(nums):
            presum+=x
            if presum in prefixSum:
                res=max(res,i-prefixSum[presum])
            else:
                prefixSum[presum]=i
        return res
        