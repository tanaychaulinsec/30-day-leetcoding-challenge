from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic=defaultdict(int)
        for num in arr:
            dic[num]+=1
        res=0
        for num in dic.keys():
            if num+1 in dic:
                res+=dic[num]
        return res       