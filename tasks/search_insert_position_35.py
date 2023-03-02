"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif nums[i] < target:
        #         continue
        #     else:
        #         return i
        # return i+1   

        #  O(log n) algorithm

        start_ind = 0
        end_ind = len(nums) - 1
        while start_ind <= end_ind:
            mid = (start_ind + end_ind) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start_ind = mid + 1
            else:
                end_ind = mid - 1

        return start_ind
