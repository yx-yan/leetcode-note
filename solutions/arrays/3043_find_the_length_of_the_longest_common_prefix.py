# Problem: 3043. Find the Length of the Longest Common Prefix
# Link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# Difficulty: Medium
# Topics: Array, Hash Table

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set()

        for arr in arr1:
            while arr not in arr1_prefix and arr > 0:
                arr1_prefix.add(arr)
                arr = arr // 10

        output = 0

        for arr in arr2:
            while arr not in arr1_prefix and arr > 0:
                arr = arr // 10
            if arr > 0:
                output = max(output, len(str(arr)))

        return output


# Time:  O(d1 + d2), where d1 and d2 are the total digits in each array
# Space: O(d1)
# Notes: Store every numeric prefix from arr1, then trim each arr2 value until
# it matches the longest stored prefix.
