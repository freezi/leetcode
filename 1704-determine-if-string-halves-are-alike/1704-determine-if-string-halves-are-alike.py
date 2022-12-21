class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        for i in range(len(s) // 2):
            c = s[i].lower()
            if c in m:
                m[c] = m.get(c) + 1
                
        for i in range(len(s) // 2, len(s)):
            c = s[i].lower()
            if c in m:
                m[c] =  m.get(c) - 1
        
        return sum(m.values()) == 0