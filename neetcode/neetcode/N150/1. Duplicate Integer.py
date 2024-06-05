class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sum = 0
        countZero = 0
        for n in nums:
            sum += n
            if n == 0:
                countZero += 1
        numSet = set(nums)

        for n in numSet:
            sum -= n

        return False if sum == 0 and countZero < 2 else True


    def hasDuplicate2(self, nums: List[int]) -> bool:
        numMap = dict()
        for n in nums:
            if numMap.get(n):
                return True
            numMap[n] = True
        return False

