class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sort = sorted(nums)
        
        return nums.index(sort[-1]) if sort[-1] >= 2 * sort[-2] else -1