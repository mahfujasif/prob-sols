from collections import defaultdict
from typing import List


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)
    #     count = defaultdict(lambda: 0)
    #     for n in nums:
    #         count[n] = count.get(n, 0) + 1
    #     print(count)
    #     start = current = min(nums)
    #     end, maxL = max(nums), 0
    #     while current <= end:
    #         print('ccn', count[current])
    #         print('s-c:', start, '-', current)
    #         if count[current] > 0:
    #             if current-start+1 > maxL:
    #                 maxL = current-start+1
    #                 print('max:', maxL)
    #         else:
    #             start = current+1
    #         current += 1
    #     return maxL
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxL = 0
        for n in nset:
            if(n-1) not in nset:
                sublength = 1
                while (n + sublength) in nset:
                    sublength += 1
                maxL = max(maxL, sublength)
        return maxL

print(Solution.longestConsecutive(Solution(),[-2, -1,1]))