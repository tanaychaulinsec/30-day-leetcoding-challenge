class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums=[x if x else -1 for x in nums]
        dict={0:-1}
        presum=res=0
        for i,x in enumerate(nums):
            presum+=x
            if presum in dict:
                res=max(res,i-dict[presum])
            else:
                dict[presum]=i
        return res