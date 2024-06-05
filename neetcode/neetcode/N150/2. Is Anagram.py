class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        ns = ''.join(sorted(s))

        t = t.lower()
        nt = ''.join(sorted(t))

        return True if ns == nt else False