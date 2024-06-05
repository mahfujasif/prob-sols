from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = dict()

        for mem in strs:
            lmem = mem.lower()
            smem = ''.join(sorted(lmem))
            lst = result.get(smem, [])
            lst.append(mem)
            result[smem] = lst

        fr = []
        for k,v in result.items():
            fr.append(v)
        return fr

print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))