class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1
        
        return ans