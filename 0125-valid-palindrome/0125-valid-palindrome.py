class Solution(object):
    def isPalindrome(self, s):
        cleaned="".join(ch.lower()for ch in s if ch.isalnum())
        return cleaned==cleaned[::-1]
        