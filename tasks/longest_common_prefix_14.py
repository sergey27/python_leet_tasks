"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)

        prefix = ""
        current_sym = ""

        for i in range(len(sorted_strs[0])):
            for j in range(len(sorted_strs)):
                if j == 0:
                    current_sym = sorted_strs[j][i]
                else:
                    if current_sym != sorted_strs[j][i]:
                        return prefix

            prefix += current_sym

        return prefix
