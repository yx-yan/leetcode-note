# Problem: 242. Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Topics: Hash Table, String, Sorting

from collections import Counter


# =========================================================================
# 方法一：逐个字母用 str.count 比较（我的第一版）
# =========================================================================
class SolutionCount:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in s:
            if s.count(c) != t.count(c):  # 每次 count 都要扫一遍整个字符串
                return False
        return True

# Time:  O(n^2)
# Space: O(1)


# =========================================================================
# 方法二：排序后比较
# =========================================================================
class SolutionSort:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time:  O(n log n)
# Space: O(n)，sorted 返回新列表


# =========================================================================
# 方法三：哈希表计数，s 加 t 减
# =========================================================================
class SolutionHashMap:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
            if count[c] < 0:  # 长度相等，某个字母不够用就一定不是
                return False
        return True

# Time:  O(n)
# Space: O(1)，最多 26 个小写字母


# =========================================================================
# 方法四：Counter 直接比较
# =========================================================================
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time:  O(n)
# Space: O(1)


# =========================================================================
# 方法五：长度 26 的数组代替哈希表
# =========================================================================
class SolutionArray:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - ord('a')] += 1
            count[ord(b) - ord('a')] -= 1
        return all(x == 0 for x in count)

# Time:  O(n)
# Space: O(1)


Solution = SolutionHashMap

# Notes: 异位词 = 每个字母出现次数相同，所以核心是「计数」。
#        方法一思路对但慢：循环里调用 str.count，每次都重扫字符串，变成 O(n^2)。
#        改进办法是一次遍历数完（方法三），而不是每个字母重新数。
#        面试先手写方法三，再说可以用 Counter 简化；只有小写字母时可用数组。
# Python: Counter(s) == Counter(t) 比较计数；count.get(c, 0) + 1 计数；
#         ord(c) - ord('a') 把字母映射到 0-25；str.count 是 O(n)，别放进循环
