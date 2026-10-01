from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)         

        for s in strs:                     
            counts = [0] * 26               

            for c in s:                     
                # TODO: add 1 to the right slot in counts
                counts[ord(c) - ord('a')] += 1
               
            groups[tuple(counts)].append(s)
            
        return list(groups.values())
