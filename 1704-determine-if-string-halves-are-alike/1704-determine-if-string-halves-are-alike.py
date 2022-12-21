class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() in m:
                m[s[l].lower()] = m.get(s[l].lower()) + 1
            if s[r].lower() in m:
                m[s[r].lower()] =  m.get(s[r].lower()) - 1
            l += 1
            r -= 1
                                
        return sum(m.values()) == 0