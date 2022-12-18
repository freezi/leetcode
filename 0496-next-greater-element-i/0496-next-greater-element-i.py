class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for num in nums1:
            j = nums2.index(num)
            c = -1
            
            while j < len(nums2):
                if nums2[j] > num:
                    c = nums2[j]
                    break
                else:
                    j += 1
                    
            ans.append(c)
        
        return ans
                