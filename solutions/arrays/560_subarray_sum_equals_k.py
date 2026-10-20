# Problem: 560. Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium
# Topics: Array, Hash Table, Prefix Sum

from collections import defaultdict
from typing import List


# =========================================================================
# 方法一：暴力，枚举起点 i，往右累加到终点 j（会超时）
# =========================================================================
class SolutionBruteForce:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):         # i：起点
            total = 0                      # 换起点，和从 0 重新算
            for j in range(i, len(nums)):  # j：终点，total 是 nums[i..j] 的和
                total += nums[j]
                if total == k:
                    count += 1
        return count

# Time:  O(n²)，n = 2×10⁴ 时约 2 亿个子数组，LeetCode 超时
# Space: O(1)


# =========================================================================
# 方法二：前缀和 + 哈希计数，固定终点，查前面有几个合适的起点
# =========================================================================
class SolutionPrefixSumHashMap:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = 0                  # 当前前缀和
        seen = defaultdict(int)  # 前面出现过的前缀和 -> 次数
        seen[0] = 1              # 一个数都没加时的前缀和，让从下标 0 开始的子数组也能被找到
        for x in nums:
            pre += x
            count += seen.get(pre - k, 0)  # 先查：前面有几个前缀和 == pre - k
            seen[pre] += 1                 # 后记：保证查到的都在当前位置之前
        return count

# Time:  O(n)
# Space: O(n)，seen 最多存 n + 1 个不同的前缀和


Solution = SolutionPrefixSumHashMap

# Notes: 子数组 = 连续的一段（不是随便挑的组合），由起点和终点唯一决定，共 n(n+1)/2 个。
#        nums[i..j] 的和 = pre[j+1] - pre[i]，所以要找 pre[i] == pre[j+1] - k，
#        和 Two Sum 一样边走边查哈希表，只是存的是「次数」而不是下标。
#        有负数，窗口变大和不一定变大，所以不能用滑动窗口。
#        我写的时候的坑：前缀和数组 + 双重循环，j 从 i 开始会数到空段，
#        k = 0 时答案偏大（[1], k = 0 得到 2）；而且仍是 O(n²)，没真正提速。
#        先记后查也会在 k = 0 时查到自己，等于又数了空段。
# Python: defaultdict 用 d[key] 读不存在的 key 会把 key: 0 插进去，
#         只查不存时用 d.get(key, 0) 或先 key in d，否则字典多出一堆没用的 key 变慢
