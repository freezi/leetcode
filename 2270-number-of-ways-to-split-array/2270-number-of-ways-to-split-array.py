class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cur = ans = 0
        summ = sum(nums)
        
        for i in range(len(nums) - 1):
            cur += nums[i]
            if cur >= summ - cur:
                ans += 1
            
        return ans