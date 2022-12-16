class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            c = 0
            
            while num:
                num //= 10
                c += 1
                
            if not c % 2:
                count += 1
        
        return count