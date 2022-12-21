class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        l = len(s)
        
        for i in range(0, l // 2):
            if s[i].lower() in m:
                m[s[i].lower()] = m.get(s[i].lower()) + 1
                
        for i in range(l // 2, l):
            if s[i].lower() in m:
                m[s[i].lower()] =  m.get(s[i].lower()) - 1
                
        return sum(m.values()) == 0