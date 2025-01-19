"""
Source: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
---
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""  # Noqa:E501

from typing import List

"""
? pseudocode:
? edge cases: [] and [x]*n
? for every i in n indexes: nums[i]-1. nums' elements are in range [1, n] so every element-1 can be a pointer.
? visit a pointed value and mark it as visited: nums[nums[i]-1] -> i: [0, n]
? if the pointed value is already marked, it means that other of nums' indexes points toward it the current index is a duplicate.
? add the current index to the result
? repeat
"""  # Noqa:E501


# Note: This approach is O(n) and O(1) space.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        stash = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                stash.append(abs(nums[i]))
            else:
                nums[index] *= -1
        return stash


#  ! O(n^2): Time Limit Exceeded
# Note: This approach is O(n^2) and O(n) space (duplicated input).
class SolutionBruteForce:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        processed = [None] * len(nums)
        result = []
        for n in nums:  # runs: O(n)
            if n in processed:  # runs: O(n) * O(n)
                result.append(n)
        return result
