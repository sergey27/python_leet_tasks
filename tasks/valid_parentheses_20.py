"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        charsDict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] in charsDict.values():
                    stack.append(s[i])
                else:
                    return False
            else:
                if s[i] in charsDict.values():
                    stack.append(s[i])
                else:
                    if stack[len(stack) - 1] != charsDict[s[i]]:
                        return False
                    else:
                        stack.pop()

        return len(stack) == 0
