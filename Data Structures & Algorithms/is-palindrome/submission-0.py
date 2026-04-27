class Solution:
    def isPalindrome(self, s: str) -> bool:

        low = "abcdefghijklmnopqrstuvwxyz"
        up = low.upper()
        digits = "0123456789"

        allowed = low + up + digits

        crunched = [c for c in s.lower() if c in allowed]
        reverse = [c for c in reversed(s.lower()) if c in allowed]
        print(crunched, reverse)

        return crunched == reverse
        