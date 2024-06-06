from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], kf: int) -> List[int]:
        mp = dict()
        for n in nums:
            c = mp.get(n, 0)
            c += 1
            mp[n] = c

        res = dict()
        for k,v in mp.items():
            lst = res.get(v, [])
            lst.append(k)
            res[v] = lst

        res = dict(sorted(res.items()))
        print(res)
        fr = []

        for keys in reversed(res):
            for x in res[keys]:
                fr.append(x)

        return fr[:kf]


print(Solution().topKFrequent([1,2], 2))