class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # I'm just gonna solve with by sorting first and I'll come back to optimize
        ans = []
        
        for num in nums:
            ans.append(num ** 2)
            
        return sorted(ans)