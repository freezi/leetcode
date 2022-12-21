class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        for i in range(len(s) // 2):
            if s[i].lower() in m:
                m[s[i].lower()] = m.get(s[i].lower()) + 1
                
        for i in range(len(s) // 2, len(s)):
            if s[i].lower() in m:
                m[s[i].lower()] =  m.get(s[i].lower()) - 1
        
        return sum(m.values()) == 0