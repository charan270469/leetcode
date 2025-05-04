class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return str(x) == str(x[::-1])


s=Solution()
s.isPalindrome(121)