# 8 周刷题打卡表

这是唯一的进度记录：做完一道题，只需在这里打卡。

**打卡**：在「打卡」列写 `✅ 日期`（独立做出）或 `🔁 日期`（看了题解，复习日重做）。留空表示没做。

**复习日**：本周的 🔁 题全部从零重写；再从两周前的题里抽 3 道重写。5 分钟内写不出来就保留 🔁。

## 总览

| 周 | 专题 | 题解目录 | 完成 | 小结 |
|---|---|---|---|---|
| 1 | [数组与哈希表](#第-1-周--数组与哈希表) | `arrays/` | /10 | |
| 2 | [双指针与滑动窗口](#第-2-周--双指针与滑动窗口) | `two_pointers/`、`sliding_window/` | /10 | |
| 3 | [栈、队列与二分查找](#第-3-周--栈队列与二分查找) | `stack_queue/`、`binary_search/` | /10 | |
| 4 | [链表](#第-4-周--链表) | `linked_list/` | /10 | |
| 5 | [二叉树](#第-5-周--二叉树) | `trees/` | /10 | |
| 6 | [回溯与堆](#第-6-周--回溯与堆) | `backtracking/`、`heap/` | /10 | |
| 7 | [图](#第-7-周--图) | `graphs/` | /10 | |
| 8 | [动态规划](#第-8-周--动态规划) | `dynamic_programming/` | /10 | |

题解目录都在 `solutions/` 下，第一次用到某个目录时再新建。每周第 6 天复习，第 7 天的加练题可选。

---

## 第 1 周 · 数组与哈希表

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 1 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | `dict`、`enumerate` | |
| 1 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | `set` | ✅ 2026-10-16 |
| 2 | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | `Counter` | ✅ 2026-10-16 |
| 2 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | `defaultdict(list)`、元组作 key | |
| 3 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | `most_common`、桶 | |
| 3 | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | `set` O(1) 查找 | |
| 4 | [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 前缀和、`accumulate` | |
| 4 | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | `[1] * n`、正反两遍 | |
| 5 | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 前缀和 + 哈希计数 | |
| 5 | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | `(r // 3, c // 3)` | |
| 6 | 复习日 | | |
| 7 | 加练：[41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)（Hard） | 原地哈希 | |

## 第 2 周 · 双指针与滑动窗口

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 8 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | `isalnum`、`lower` | |
| 8 | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | `a, b = b, a` | |
| 9 | [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 相向指针 | |
| 9 | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 移动短板 | |
| 10 | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | 从后往前填 | |
| 10 | [15. 3Sum](https://leetcode.com/problems/3sum/) | 排序 + 去重 | |
| 11 | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | `float('inf')` | |
| 11 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 可变窗口 + `set` | |
| 12 | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | `ord(c) - ord('A')` | |
| 12 | [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | 固定窗口 | |
| 13 | 复习日 | | |
| 14 | 加练：[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)（Hard） | 窗口收缩 | |

## 第 3 周 · 栈、队列与二分查找

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 15 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | `list` 当栈 | |
| 15 | [155. Min Stack](https://leetcode.com/problems/min-stack/) | 设计类、`self` | |
| 16 | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | 双栈 | |
| 16 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | `int(a / b)` | |
| 17 | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | 单调栈 | |
| 17 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 栈存下标 | |
| 18 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | `(l + r) // 2` | |
| 18 | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | `bisect_left` | |
| 19 | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | `bisect_right` | |
| 19 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 判断有序半边 | |
| 20 | 复习日 | | |
| 21 | 加练：[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 二分答案 | |

## 第 4 周 · 链表

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 22 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 多重赋值顺序 | |
| 22 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | `dummy` 节点 | |
| 23 | [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | 快慢指针 | |
| 23 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | `while fast and fast.next` | |
| 24 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 前后指针 | |
| 24 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | `divmod`、`x or 0` | |
| 25 | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | 找中点 + 反转 | |
| 25 | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | 拆分、反转、合并 | |
| 26 | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 节点作 `dict` key | |
| 26 | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | `OrderedDict` | |
| 27 | 复习日 | | |
| 28 | 加练：[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)（Hard） | 分段反转 | |

## 第 5 周 · 二叉树

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 29 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 递归 | |
| 29 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 同时交换 | |
| 30 | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | 递归版 + 迭代版 | |
| 30 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | `deque`、按层循环 | |
| 31 | [100. Same Tree](https://leetcode.com/problems/same-tree/) | 短路 `and` | |
| 31 | [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | 内部辅助函数 | |
| 32 | [112. Path Sum](https://leetcode.com/problems/path-sum/) | 递归传参 | |
| 32 | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | `nonlocal` | |
| 33 | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 上下界 | |
| 33 | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 后序遍历 | |
| 34 | 复习日 | | |
| 35 | 加练：[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 下标映射 | |

## 第 6 周 · 回溯与堆

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 36 | [78. Subsets](https://leetcode.com/problems/subsets/) | `path[:]` 拷贝 | |
| 36 | [46. Permutations](https://leetcode.com/problems/permutations/) | `used` 数组 | |
| 37 | [77. Combinations](https://leetcode.com/problems/combinations/) | `start` 参数 | |
| 37 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | 剪枝 | |
| 38 | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 字符串递归 | |
| 38 | [79. Word Search](https://leetcode.com/problems/word-search/) | 网格 DFS、标记还原 | |
| 39 | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | `heapq` | |
| 39 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 大小为 k 的堆 | |
| 40 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 取负数做大顶堆 | |
| 40 | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard） | `(val, i, node)` | |
| 41 | 复习日 | | |
| 42 | 加练：[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)（Hard） | 双堆 | |

## 第 7 周 · 图

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 43 | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | 方向数组 | |
| 43 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | 网格 DFS / BFS | |
| 44 | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | DFS 返回值 | |
| 44 | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 多源 BFS | |
| 45 | [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | 邻接表 | |
| 45 | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | `dict` 记录克隆 | |
| 46 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | 拓扑排序、入度 | |
| 46 | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 输出拓扑序 | |
| 47 | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | 并查集 | |
| 47 | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 路径压缩 | |
| 48 | 复习日 | | |
| 49 | 加练：[743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra | |

## 第 8 周 · 动态规划

| Day | 题目 | Python 重点 | 打卡 |
|---|---|---|---|
| 50 | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | `@cache` vs 递推 | |
| 50 | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | 滚动变量 | |
| 51 | [198. House Robber](https://leetcode.com/problems/house-robber/) | 状态定义 | |
| 51 | [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | 切片复用 | |
| 52 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | `float('inf')` 初始化 | |
| 52 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | `bisect` 优化 | |
| 53 | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | 二维列表初始化 | |
| 53 | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | 原地 DP | |
| 54 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 多一行一列 | |
| 54 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 背包倒序 | |
| 55 | 复习日 | | |
| 56 | 结业自测：每个专题抽 1 道 + 所有 🔁 题，限时重写 | | |

---

## 计划外

每日一题等不在计划里的题记在这里。

| 题目 | 题解 | 打卡 |
|---|---|---|
| [2196. Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/) | [trees](solutions/trees/2196_create_binary_tree_from_descriptions.py) | ✅ |
| [2540. Minimum Common Value](https://leetcode.com/problems/minimum-common-value/) | [two_pointers](solutions/two_pointers/2540_minimum_common_value.py) | ✅ |
| [2657. Find the Prefix Common Array of Two Arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) | [arrays](solutions/arrays/2657_find_the_prefix_common_array_of_two_arrays.py) | ✅ |
| [2904. Shortest and Lexicographically Smallest Beautiful String](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/) | [sliding_window](solutions/sliding_window/2904_shortest_and_lexicographically_smallest_beautiful_string.py) | ✅ |
| [3043. Find the Length of the Longest Common Prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) | [arrays](solutions/arrays/3043_find_the_length_of_the_longest_common_prefix.py) | ✅ |
| [3660. Jump Game IX](https://leetcode.com/problems/jump-game-ix/) | [stack_queue](solutions/stack_queue/3660_jump_game_ix.py) | ✅ |
