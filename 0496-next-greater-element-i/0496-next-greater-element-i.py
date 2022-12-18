class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            c = -1
            
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    c = nums2[j]
                    break
                else:
                    j += 1
                    
            ans.append(c)
        
        return ans
                