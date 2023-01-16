class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = sorted(s)
        km = sorted(t)
        if hm == km:
            return True
        else:
            return False