class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start = 0
        result = 0
        
        for i in range(len(s)):
            if i - start + 1 == 3:
                visited = {}
                
                for j in range(start, i + 1):
                    if s[j] not in visited:
                        visited[s[j]] = 1
                    else:
                        break
                        
                if len(visited) == 3:
                    result += 1
                start += 1
        
        return result