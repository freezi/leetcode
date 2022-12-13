class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().split(' ')
        newStr = ''
        
        for index, word in enumerate(s):
            for x in word:
                if x.isalnum():
                    newStr += x
        
        return newStr == newStr[::-1] 