# Problem: 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Topics: Array, Hash Table, Heap (Priority Queue), Bucket Sort, Counting

from collections import Counter
from typing import List


# =========================================================================
# 方法一：手写计数 + 按次数排序
# =========================================================================
class SolutionSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        # items() 给出 (数字, 次数)，按次数从大到小排
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [pair[0] for pair in sorted_counts[:k]]

# Time:  O(n log n)，排序最多 n 个不同的数
# Space: O(n)


# =========================================================================
# 方法二：Counter.most_common
# =========================================================================
class SolutionCounter:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, cnt in Counter(nums).most_common(k)]

# Time:  O(n log k)，most_common(k) 内部用堆
# Space: O(n)


# =========================================================================
# 方法三：桶排序，下标 = 出现次数
# =========================================================================
class SolutionBucket:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]  # 次数最多是 len(nums)
        for num, cnt in counts.items():
            buckets[cnt].append(num)

        res = []
        for cnt in range(len(buckets) - 1, 0, -1):  # 从高频往低频取
            for num in buckets[cnt]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

# Time:  O(n)，次数有上限 n，不用比较排序
# Space: O(n)


Solution = SolutionSort

# Notes: 先计数，再按次数挑前 k 个。排序 O(n log n) 最直观；
#        次数不会超过 n，所以可以把次数当下标放进桶里，做到 O(n)。
# Python: counts.items() 返回 (key, value) 对，sorted 排完得到新 list；
#         sorted(..., key=lambda x: x[1], reverse=True) 按 value 降序；
#         for num, cnt in ... 直接解包，比 pair[0] 好读；
#         .items() 是方法名不能改，for 后面的变量名可以随便起
