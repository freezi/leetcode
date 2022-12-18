class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        
        for i in range(len(temps) - 1, -1, -1):
            while len(stack) and stack[-1][0] <= temps[i]:
                stack.pop()
            
            if not len(stack):
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            
            stack.append([temps[i], i])
        
        return ans