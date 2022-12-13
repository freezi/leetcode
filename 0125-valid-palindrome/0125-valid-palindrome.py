class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:    
                left += 1
                right -= 1
            
        return True
        
        
#         s = s.lower().split(' ')
#         newStr = ''
        
#         for index, word in enumerate(s):
#             for x in word:
#                 if x.isalnum():
#                     newStr += x
        
#         return newStr == newStr[::-1] 