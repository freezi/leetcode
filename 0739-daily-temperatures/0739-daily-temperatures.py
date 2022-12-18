class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        
        for i in range(len(temps) - 1, -1, -1):
            while len(stack) != 0 and stack[-1][0] <= temps[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            
            stack.append([temps[i], i])
        
        return ans