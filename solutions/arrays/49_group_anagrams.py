# Problem: 49. Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Topics: Array, Hash Table, String, Sorting

from collections import defaultdict
from typing import List


# =========================================================================
# 方法一：排序后的字符串作 key
# =========================================================================
class SolutionSort:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))  # sorted 返回 list，拼回 str 才能当 key
            groups[key].append(s)
        return list(groups.values())

# Time:  O(n * k log k)，n 个词，每个词最长 k
# Space: O(n * k)


# =========================================================================
# 方法二：26 个字母的计数元组作 key
# =========================================================================
class SolutionCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)  # list 不可哈希，转 tuple
        return list(groups.values())

# Time:  O(n * k)，省掉了排序
# Space: O(n * k)


Solution = SolutionCount

# Notes: 给每个词算一个「指纹」，异位词指纹相同，按指纹分组。
#        指纹可以是排序后的字符串，也可以是 26 个字母的计数。
#        接着 242 的思路：判断两个词用计数，分组就把计数当 dict 的 key。
# Python: defaultdict(list) 省掉「key 不存在先建空列表」；
#         dict 的 key 必须可哈希，list 不行，要转 tuple 或 str；
#         groups.values() 是视图，要 list() 包一层
