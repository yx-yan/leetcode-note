# Problem: 217. Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting

from typing import List


# =========================================================================
# 方法一：哈希集合，边遍历边记录
# =========================================================================
class SolutionHashSet:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # 只关心「见没见过」，不需要 dict 的 value
        for num in nums:
            if num in seen:
                return True  # 遇到重复立即返回
            seen.add(num)
        return False

# Time:  O(n)
# Space: O(n)


# =========================================================================
# 方法二：一行，比较去重前后的长度
# =========================================================================
class SolutionOneLiner:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Time:  O(n)，但总要建完整个集合，无法提前退出
# Space: O(n)


# =========================================================================
# 方法三：排序后比较相邻元素
# =========================================================================
class SolutionSort:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # 会修改输入
        return any(nums[i] == nums[i - 1] for i in range(1, len(nums)))

# Time:  O(n log n)
# Space: O(1) 额外空间（不计排序内部开销）


Solution = SolutionHashSet

# Notes: 只判断「是否出现过」用 set；需要计数或存下标时才用 dict。
#        方法一能提前退出；方法二写法最短；方法三用时间换空间。
#        实测方法二通常比方法一快约 5 倍（1e5 个无重复元素：0.5ms vs 2.4ms）：
#        set(nums) 在 C 里一次遍历完，方法一每个元素都要走 Python 字节码
#        （取元素、in 判断、调用 add）。只有重复出现得很早时方法一才更快。
#        复杂度相同时，Python 的内置函数通常比手写循环快。
# Python: set() / s.add(x) / x in s；len(set(nums)) != len(nums) 判重；
#         any(生成器) 短路判断
