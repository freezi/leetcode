class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f = max(nums)
        nums[nums.index(f)] = 0
        s = max(nums)
        
        return (f - 1) * (s - 1)