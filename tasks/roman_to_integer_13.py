"""
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        numbers_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        numbers = [numbers_dict[char] for char in s]

        sum = 0

        for i in range(len(numbers)):
            if i < len(numbers) - 1 and numbers[i] < numbers[i + 1]:
                sum -= numbers[i]
                continue
            sum += numbers[i]

        return sum