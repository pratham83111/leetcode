class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        a=len(a[-1])
        return a