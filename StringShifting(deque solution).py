from collections import deque
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:  
        res=deque(s)
        for direction, amount in shift:
            if direction ==0:
                res.rotate(-amount)
            else:
                res.rotate(amount)
        return "".join(res) 