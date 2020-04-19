class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        lshifts = 0
        rshifts = 0
        
        for i in shift:
            
            if i[0] == 0:
                lshifts += i[1]
            else:
                rshifts += i[1]
            
        if rshifts == lshifts:
            return s
        
        if rshifts > lshifts:
            r = (rshifts -lshifts) % len(s)
            return s[len(s)-r:] + s[:len(s)-r]
        else:
            l = (lshifts-rshifts) % len(s)
            return s[l:]+s[:l]