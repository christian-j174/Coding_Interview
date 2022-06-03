class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str( x )
        return x == x[::-1]



x = Solution()
print(x.isPalindrome(121))