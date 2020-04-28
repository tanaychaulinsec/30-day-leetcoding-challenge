from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.od=OrderedDict()
        self.s=set()
        for n in nums:
            self.add(n)
            
    def showFirstUnique(self) -> int:
        if len(self.od)==0: return -1
        else:
            for i in self.od:
                return i
    
    def add(self, value: int) -> None:
        if value not in self.s:
            self.s.add(value)
            self.od[value]=None
        else:
            self.od.pop(value,None)