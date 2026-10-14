# Problem: 2540. Minimum Common Value
# Link: https://leetcode.com/problems/minimum-common-value/
# Difficulty: Easy
# Topics: Two Pointers, Array

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1


# Time:  O(m + n)
# 双指针遍历，每次循环至少推进一个指针，总步数不超过两个数组长度之和。
#
# Space: O(1)
# 只使用常数个额外变量。
#
# Notes: 两个数组都有序，比较当前元素后移动较小值所在的指针即可。
