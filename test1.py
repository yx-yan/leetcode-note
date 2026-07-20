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
        cur = self
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        return " -> ".join(values)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Utils:
    """提供数组与链表、二叉树之间的互相转换"""
    @staticmethod
    def to_linked_list(arr: list) -> Optional[ListNode]:
        if not arr: return None
        head = ListNode(arr[0])
        cur = head
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return head

    @staticmethod
    def to_list(head: Optional[ListNode]) -> list:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    @staticmethod
    def to_tree(arr: list) -> Optional[TreeNode]:
        if not arr: return None
        nodes = [TreeNode(val) if val is not None else None for val in arr]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

# =========================================================================
# 2. 你的 Solution 类 (直接从 LeetCode 粘贴)
# =========================================================================
# @lc code=start
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        raise NotImplementedError("Add the solution under test here")
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
        (([1,3,2], 2), 4),
        (([4,2,5,1], 3), 12)
    ]

    run_test_engine(TARGET_METHOD, my_test_cases)
