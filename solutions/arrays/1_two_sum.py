# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topics: Array, Hash Table

from typing import List


# =========================================================================
# 方法一：暴力枚举
# =========================================================================
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)

        for i in range(m):
            match = target - nums[i]
            for j in range(i + 1, m):
                if nums[j] == match:
                    return [i, j]

# Time:  O(n^2)
# Space: O(1)


# =========================================================================
# 方法二：哈希表
# =========================================================================
class SolutionHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 见过的数 -> 下标
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

# Time:  O(n)
# Space: O(n)


Solution = SolutionHashMap
