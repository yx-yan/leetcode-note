# Problem: 128. Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Topics: Array, Hash Table, Union Find

from typing import List


# =========================================================================
# 方法一：排序 + 一次遍历（不满足题目 O(n) 要求）
# =========================================================================
class SolutionSort:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)  # 不改动调用者的列表, 复杂度nlogn
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # 重复元素跳过，不打断也不计数
            if nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                cur = 1  # 断开就重置
            best = max(best, cur)
        return best

# Time:  O(n log n)，瓶颈在排序
# Space: O(n)，sorted 返回新列表


# =========================================================================
# 方法二：哈希集合 + 只从起点往后数（标准答案）
# =========================================================================
class SolutionHashSet:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for x in num_set:  # 遍历 set 而不是 nums，避免重复起点被数多次
            if x - 1 not in num_set:  # x 是一段的起点
                y = x
                while y + 1 in num_set:
                    y += 1
                best = max(best, y - x + 1)
        return best

# Time:  O(n)，每个数最多被 while 访问一次
# Space: O(n)


# =========================================================================
# 方法三：哈希表维护区间端点的长度（适合数据流）
# =========================================================================
class SolutionBoundary:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}  # 只保证每段两个端点上的长度是对的
        best = 0
        for x in nums:
            if x in length:
                continue
            left = length.get(x - 1, 0)   # 左边那段的长度
            right = length.get(x + 1, 0)  # 右边那段的长度
            total = left + right + 1
            # x 把左右两段连起来，更新新段的两个端点
            length[x] = length[x - left] = length[x + right] = total
            best = max(best, total)
        return best

# Time:  O(n)
# Space: O(n)


# =========================================================================
# 方法四：并查集，把 x 和 x + 1 合并
# =========================================================================
class SolutionUnionFind:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {x: x for x in nums}
        size = {x: 1 for x in parent}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 路径压缩
                x = parent[x]
            return x

        for x in parent:
            if x + 1 in parent:
                rx, ry = find(x), find(x + 1)
                if rx != ry:
                    if size[rx] < size[ry]:  # 小的挂到大的下面
                        rx, ry = ry, rx
                    parent[ry] = rx
                    size[rx] += size[ry]

        return max(size.values(), default=0)

# Time:  ≈O(n)，find 均摊接近常数
# Space: O(n)


Solution = SolutionHashSet

# Notes: 排序后连续的数挨在一起，但排序就要 O(n log n)。
#        O(n) 的关键：放进 set，只在 x - 1 不存在（x 是起点）时才往后数，
#        这样每个数只被数一次。端点哈希表适合数字一个个到达的场景；
#        并查集能做但大材小用。
#        我第一版的坑：断开时应该直接重置 count，
#        不要再套一层 if count > output。
# Python: if x - 1 not in num_set 用 set 的 O(1) 查找判断起点；
#         a[x] = a[y] = a[z] = v 链式赋值，同一个值赋给多个位置；
#         max(iterable, default=0) 空序列时返回 default，不会报错
