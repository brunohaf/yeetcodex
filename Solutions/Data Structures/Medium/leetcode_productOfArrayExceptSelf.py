from typing import List


class SolutionAlmost:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # O(3n) = O(n)
        answer = [1 for _ in range(len(nums))]  # O(n)
        for right in range(len(nums)-2, -1, -1):  # O(n)
            answer[right] = answer[right + 1]*nums[right + 1]
        prefix = 1
        for left in range(1, len(nums)+1):  # O(n)
            answer[left-1] *= prefix
            prefix *= nums[left-1]
        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # O(3n) = O(n)
        answer = [1 for _ in range(len(nums))]  # O(n), space: O(1)
        prefix = 1
        right, left = len(nums) - 2, 1
        while True:  # O(n)
            if left <= len(nums):
                answer[left - 1] *= prefix
                prefix *= nums[left - 1]
            if right >= 0:
                answer[right] = answer[right + 1] * nums[right + 1]
            if right < 0 and left > len(nums)+1:
                break
            right -= 1
            left += 1

        return answer


testcases = [
    [1, 2, 3, 4], [-1, 1, 0, -3, 3],
]

for test in testcases:
    print(Solution().productExceptSelf(test))
