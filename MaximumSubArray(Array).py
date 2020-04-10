class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end_here=max_so_far=0
        for i in nums:
            max_end_here+=i
            if max_end_here<0:
                max_end_here=0
            if max_so_far<max_end_here:
                max_so_far=max_end_here
        if max_so_far==0:
            return max(nums)
        return max_so_far
        