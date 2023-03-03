"""
Given an integer x, return true if x is a
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def reverseNumber(self, num: int) -> int:
        new_number = 0
        while num != 0:
            new_number *= 10
            current_number = num % 10
            new_number += current_number
            num //= 10
        return new_number

    def isPalindrome(self, x: int) -> bool:
        # v1
        # return str(x) == str(x)[::-1]

        # v2
        if x < 0:
            return False
        return x == self.reverseNumber(x)


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))

