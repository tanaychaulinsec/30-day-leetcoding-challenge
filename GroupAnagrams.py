from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            if key not in dic:
                dic[key]=[word]
            else:
                dic[key].append(word)
        return list(dic.values())        