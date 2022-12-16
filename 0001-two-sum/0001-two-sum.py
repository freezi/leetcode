class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for i, j in enumerate(nums):
            if target - j in m:
                return [m[target - j], i]
            else:
                m[j] = i