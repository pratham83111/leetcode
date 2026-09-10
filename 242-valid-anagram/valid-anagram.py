class Solution(object):
    def isAnagram(self, s, t):
        self.s = s
        self.t = t
        return sorted(s)==sorted(t)