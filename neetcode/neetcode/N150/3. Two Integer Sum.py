from collections import deque
from typing import List


class Solution:


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i, n in enumerate(nums):
            d = target - n
            if d in mp:
                return [mp[d], i]
            mp[n] = i

    def buildIdx(self, numL: List[int]):
        idx = dict()

        for i, n in enumerate(numL):
            q = deque()
            iq = idx.get(n, q)
            iq.append(i)
            idx[n] = iq
        return idx

    def getIdx(self, idx, n):
        q = deque()
        iq = idx.get(n, q)
        return -1 if len(iq) < 1 else iq.pop()

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idx = self.buildIdx(nums)
        nums = sorted(nums)
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                s, t = self.getIdx(idx, nums[i]), self.getIdx(idx, nums[j])
                return [s, t] if s <= t else [t, s]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return [0, 0]







nums = [3, 4, 5, 6]
target = 7
sol = Solution()
print(sol.twoSum(nums, target))
