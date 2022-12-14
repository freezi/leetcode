class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = cur = prev = 0
        mid = (len(nums1) + len(nums2)) // 2 + 1
        
        for k in range(mid):
            prev = cur
            if j == len(nums2) or (i != len(nums1) and nums1[i] <= nums2[j]):
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
            
        if (len(nums1) + len(nums2)) % 2:
            return cur
        else:
            return (cur + prev) / 2