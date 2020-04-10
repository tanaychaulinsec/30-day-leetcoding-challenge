class Solution:
    def isHappy(self, n: int) -> bool:
        dic={}
        while n!=1 and n not in dic:
            dic[n]=True
            a=list(str(n))
            n=sum(map(lambda x: int(x)**2,a))
        return n==1 