from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic=defaultdict(int)
        count=running_sum=0
        for num in nums:
            running_sum+=num
            if running_sum-k in dic:
                count+=dic[running_sum-k]
            if running_sum==k:
                count+=1
            dic[running_sum]+=1
        return count