import time
import inspect
from typing import  List, Optional, Dict, Any, Union
import bisect # 二分查找模块
import functools # 用于缓存
import random
from collections import Counter, defaultdict, deque
from itertools import chain

# =========================================================================
# 1. LeetCode 标准数据结构 (链表与二叉树)
# =========================================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Utils:
    """提供数组与链表、二叉树之间的互相转换"""

    @staticmethod
    def to_linked_list(values: list) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    @staticmethod
    def to_list(head: Optional[ListNode]) -> list:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    @staticmethod
    def to_tree(values: list) -> Optional[TreeNode]:
        if not values:
            return None
        nodes = [TreeNode(value) if value is not None else None for value in values]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()
        return root


# =========================================================================
# 2. 你的 Solution 类 (直接从 LeetCode 粘贴)
# =========================================================================
# @lc code=start
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # sort the input
        s1 = sorted(s)

        output = ""
        used = []
        open = 0
        for i in range(n):       # target loop
            matched = False
            for j in range(n):   # input loop
                if open == 0:
                    if j not in used:
                        if target[i] == s1[j]:
                            output = output + s1[j]
                            used.append(j)
                            matched = True
                            break
                        if target[i] < s1[j]:
                            open = 1
                            output = output + s1[j]
                            used.append(j)
                            matched = True
                            break
                else:
                    if j not in used:
                        output = output + s1[j]
                        used.append(j)
                        matched = True
                        break
            if not matched:
                break

        # Asking AI for help
        if len(output) < n:
            for x in range(len(output) - 1, -1, -1):
                used_index = used[x]

                for j in range(used_index + 1, n):
                    if j not in used[:x] and s1[j] > target[x]:
                        output = output[:x] + s1[j]

                        remaining = []
                        used_before = used[:x] + [j]

                        for k in range(n):
                            if k not in used_before:
                                remaining.append(s1[k])

                        output += ''.join(remaining)
                        return output

            return ""

        
        found = False
        if output == target:
            for x in range(n - 2, -1, -1):
                for y in range(n - 1, x, -1):
                    if output[x] < output[y]:
                        output = output[:x] + output[y] + ''.join(sorted(output[x:y] + output[y + 1:]))
                        found = True
                        break
                if found:
                    break
        if output == target:
            return ""
        return output
# @lc code=end

# =========================================================================
# 3. 自动化测试引擎 (无需修改)
# =========================================================================
def run_test_engine(method_name: str, test_cases: list):
    sol = Solution()
    # 获取类中的方法
    func = getattr(sol, method_name)
    
    print(f"\n{'='*20} 测试开始: {method_name} {'='*20}")
    for i, (args, expected) in enumerate(test_cases):
        # 统一处理参数：如果 args 不是元组，包装成元组以便解包
        actual_args = args if isinstance(args, tuple) else (args,)
        
        start = time.perf_counter()
        try:
            # 执行代码
            actual = func(*actual_args)
            end = time.perf_counter()

            if isinstance(actual, ListNode):
                actual = Utils.to_list(actual)
            elif actual is None and isinstance(expected, list):
                actual = []
            
            # 结果对比 (如果是 TreeNode 或 ListNode，可能需要自定义对比，这里仅支持基础对比)
            is_correct = actual == expected
            status = "✅ PASSED" if is_correct else "❌ FAILED"
            
            print(f"Case {i+1}: {status} | 耗时: {(end-start)*1000:.4f}ms")
            if not is_correct:
                print(f"   输入: {args}")
                print(f"   预期: {expected}")
                print(f"   实际: {actual}")
        except Exception as e:
            print(f"Case {i+1}: 💥 ERROR | 错误类型: {type(e).__name__}: {e}")
    print(f"{'='*55}\n")

# =========================================================================
# 4. 配置测试用例 (在此手动填写)
# =========================================================================
if __name__ == "__main__":
    # 自动检测 Solution 类中定义的第一个方法
    _methods = [name for name, _ in inspect.getmembers(Solution, predicate=inspect.isfunction)]
    TARGET_METHOD = _methods[0]

    my_test_cases = [
        (("aab", "abb"), "baa"),
        (("aab", "aab"), "aba"),
        (("aab", "aba"), "baa"),
        (("abc", "bba"), "bca"),
        (("leet", "code"), "eelt"),
        (("baba", "bbaa"), ""),
        (("ab", "ab"), "ba")
    ]

    run_test_engine(TARGET_METHOD, my_test_cases)
