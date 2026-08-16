class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = [co.lower() for co in s if co.isalnum()]
        return f == f[::-1]
        