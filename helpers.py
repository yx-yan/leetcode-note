"""playground.py 用到的公共工具：LeetCode 数据结构、转换函数和测试引擎。"""

import time
from typing import Optional


# =========================================================================
# LeetCode 标准数据结构 (链表与二叉树)
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
# 自动化测试引擎
# =========================================================================
def run_test_engine(solution_cls, test_cases: list):
    """运行 solution_cls 中定义的第一个公开方法，逐条对比 (输入, 预期) 用例。"""
    method_name = next(
        name for name, value in vars(solution_cls).items()
        if callable(value) and not name.startswith("_")
    )
    func = getattr(solution_cls(), method_name)

    print(f"\n{'='*20} 测试开始: {method_name} {'='*20}")
    for i, (args, expected) in enumerate(test_cases):
        # 统一处理参数：如果 args 不是元组，包装成元组以便解包
        actual_args = args if isinstance(args, tuple) else (args,)

        start = time.perf_counter()
        try:
            actual = func(*actual_args)
            end = time.perf_counter()

            if isinstance(actual, ListNode):
                actual = Utils.to_list(actual)
            elif actual is None and isinstance(expected, list):
                actual = []

            # 仅支持基础类型对比；返回 TreeNode 时需自行转换
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
