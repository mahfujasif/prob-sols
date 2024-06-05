from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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