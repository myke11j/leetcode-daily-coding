class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroFilledSubarrayCount = 0
        consecutiveZeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroFilledSubarrayCount = zeroFilledSubarrayCount + consecutiveZeroes + 1
                consecutiveZeroes += 1
            else:
                consecutiveZeroes = 0
        
        return zeroFilledSubarrayCount
