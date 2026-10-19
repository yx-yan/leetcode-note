# Problem: 303. Range Sum Query - Immutable
# Link: https://leetcode.com/problems/range-sum-query-immutable/
# Difficulty: Easy
# Topics: Array, Design, Prefix Sum

from itertools import accumulate
from typing import List


# =========================================================================
# 方法一：每次查询现加（暴力）
# =========================================================================
class NumArrayBruteForce:
    def __init__(self, nums: List[int]):
        self.nums = nums  # 存到 self 上，sumRange 才能用

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])  # 切片右端是开区间，要 +1

# Time:  __init__ O(1)，每次 sumRange O(n)
# Space: O(1)，只存引用


# =========================================================================
# 方法二：前缀和（标准答案）
# =========================================================================
class NumArrayPrefixSum:
    def __init__(self, nums: List[int]):
        # table[i] = 前 i 个数的和（不含 nums[i]），开头补 0
        self.table = [0]
        for i in range(len(nums)):
            self.table.append(self.table[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        # 前 right + 1 个的和 - 前 left 个的和 = nums[left..right]
        return self.table[right + 1] - self.table[left]

# Time:  __init__ O(n)，每次 sumRange O(1)
# Space: O(n)


# =========================================================================
# 方法三：前缀和，用 accumulate 一行建表
# =========================================================================
class NumArrayAccumulate:
    def __init__(self, nums: List[int]):
        self.table = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.table[right + 1] - self.table[left]

# Time:  __init__ O(n)，每次 sumRange O(1)
# Space: O(n)


NumArray = NumArrayPrefixSum

# Notes: 设计题：__init__ 只调用一次，sumRange 会被调用很多次，
#        所以把重复计算挪到 __init__ 里预处理一次。
#        前缀和表开头补一个 0，让 table[i] 表示「前 i 个数的和」，
#        区间和就是 table[right + 1] - table[left]，left = 0 也不用特判。
#        我第一版的坑：
#        1. 用 table[i] = ... 往空位置赋值，报 IndexError，新增元素要用 append；
#        2. 表里存「含 nums[i]」的和，减法少算一位；
#           改成 table[left - 1] 时 left = 0 会取到 table[-1]（最后一个），悄悄算错。
# Python: lst[i] = x 只能改已有位置，新增用 lst.append(x)；
#         lst[-1] 是最后一个元素，下标算成 -1 不会报错；
#         accumulate(nums, initial=0) 直接得到开头带 0 的前缀和
