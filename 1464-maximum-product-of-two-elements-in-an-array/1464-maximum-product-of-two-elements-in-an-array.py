class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f = s = 0
        
        for num in nums:
            f, s = max(num, f, s), max(s, min(f, num))
        
        return (f - 1) * (s - 1)
#         f = max(nums)
#         nums[nums.index(f)] = 0
#         s = max(nums)
        
#         return (f - 1) * (s - 1)