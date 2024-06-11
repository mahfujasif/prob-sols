#sol 1
from typing import List

#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         p, zi = 1, set()
#         for i, n in enumerate(nums):
#             if n == 0:
#                 zi.add(i)
#                 n = 1
#             p *= n
#         res = []
#         for i, n in enumerate(nums):
#             if n == 0:
#                 zi.remove(i)
#                 if len(zi) == 0:
#                     res.append(p)
#                 else:
#                     res.append(0)
#                 zi.add(i)
#             elif len(zi) != 0:
#                 res.append(0)
#             else:
#                 res.append(p//n)
#         return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        pf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * pf
            pf = pf * nums[i]
        return res
#[1,2,6,24]
print(Solution().productExceptSelf([2,3,4,5]))