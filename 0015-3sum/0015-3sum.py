class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]
        
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return ans