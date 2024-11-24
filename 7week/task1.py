"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        len_arr = len(arr)
        total = sum(arr[:k])
        count = 1 if total / k >= threshold else 0

        for i in range(k, len_arr):
            total += arr[i] - arr[i - k]
            if total / k >= threshold:
                count += 1

        return count
