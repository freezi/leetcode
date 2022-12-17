class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # I'm just gonna solve by sorting first and I'll come back to optimize
#         ans = []
        
#         for num in nums:
#             ans.append(num ** 2)
            
#         return sorted(ans)
        ans, l, r, i = [None] * len(nums), 0, len(nums) - 1, len(nums) - 1
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] ** 2
                l += 1
            else:
                ans[i] = nums[r] ** 2
                r -= 1
            i -= 1
        
        return ans