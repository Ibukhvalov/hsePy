"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/rotate-array/description/
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
