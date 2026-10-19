"""playground.py 用到的公共工具：常用库、LeetCode 数据结构、转换函数和测试引擎。

playground.py 只需 `from helpers import *`，就能拿到 LeetCode 环境里常用的
库（List、Counter、heapq……）。脚本运行结束时，会自动用 `tests` 测试 `Solution`。
"""

import atexit
import bisect
import functools
import heapq
import itertools
import json
import math
import re
import sys
import time
import traceback
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from math import inf
from typing import Dict, List, Optional, Set, Tuple

__all__ = [
    "List", "Optional", "Dict", "Set", "Tuple",
    "Counter", "defaultdict", "deque",
    "bisect", "functools", "heapq", "itertools", "math",
    "cache", "lru_cache", "inf",
    "ListNode", "TreeNode", "Utils", "run_test_engine", "run_design_test_engine",
]


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
# 解析 LeetCode 题面里的 Example 文本
# =========================================================================
def _split_top_level(text: str) -> list:
    """按最外层逗号切分，忽略括号和字符串里的逗号。"""
    parts, depth, in_str, escaped, start = [], 0, False, False, 0
    for i, ch in enumerate(text):
        if in_str:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return [part.strip() for part in parts if part.strip()]


def _parse_value(text: str):
    """LeetCode 的字面量（true/false/null、双引号字符串）转成 Python 值。"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        import ast
        return ast.literal_eval(text)


def parse_examples(text: str) -> list:
    """把粘贴的 "Input: a = 1, b = [2]  Output: 3" 文本转成 [((1, [2]), 3), ...]。"""
    text = text.replace("\xa0", " ")
    pattern = r"Input:?\s*(.*?)\s*Output:?\s*(.*?)\s*(?:\n|$)"
    cases = []
    for raw_input, raw_output in re.findall(pattern, text, re.S):
        args = []
        for part in _split_top_level(raw_input.replace("\n", " ")):
            name, sep, value = part.partition("=")
            args.append(_parse_value((value if sep else name).strip()))
        cases.append((tuple(args), _parse_value(raw_output)))
    return cases


def parse_design_examples(text: str) -> list:
    """把设计题的 Example（操作名一行、参数一行、Output 一行）转成 [(ops, args, expected), ...]。"""
    text = text.replace("\xa0", " ")
    pattern = r"Input:?\s*\n\s*(\[.*\])\s*\n\s*(\[.*\])\s*\n\s*Output:?\s*\n\s*(\[.*\])"
    return [
        tuple(_parse_value(part) for part in match)
        for match in re.findall(pattern, text)
    ]


# =========================================================================
# 自动化测试引擎
# =========================================================================
def run_test_engine(solution_cls, test_cases):
    """运行 solution_cls 中定义的第一个公开方法，逐条对比 (输入, 预期) 用例。

    test_cases 可以是 [(输入, 预期), ...]，也可以是直接粘贴的题面 Example 文本。
    """
    if isinstance(test_cases, str):
        test_cases = parse_examples(test_cases)
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
        except Exception:
            print(f"Case {i+1}: 💥 ERROR | 输入: {args}")
            print(traceback.format_exc())
    print(f"{'='*55}\n")


def run_design_test_engine(namespace, test_cases):
    """设计题：按 ops 依次构造对象、调用方法，逐次对比返回值。

    namespace 里要有与 ops[0] 同名的类；test_cases 可以是
    [(ops, args, expected), ...]，也可以是直接粘贴的题面 Example 文本。
    """
    if isinstance(test_cases, str):
        test_cases = parse_design_examples(test_cases)

    print(f"\n{'='*20} 设计题测试开始 {'='*20}")
    for i, (ops, args, expected) in enumerate(test_cases):
        cls = getattr(namespace, ops[0])
        start = time.perf_counter()
        try:
            obj = cls(*args[0])
            actual = [None]
            for op, op_args in zip(ops[1:], args[1:]):
                actual.append(getattr(obj, op)(*op_args))
            end = time.perf_counter()

            is_correct = actual == expected
            status = "✅ PASSED" if is_correct else "❌ FAILED"
            print(f"Case {i+1}: {status} | 耗时: {(end-start)*1000:.4f}ms")
            if not is_correct:
                for op, op_args, want, got in zip(ops, args, expected, actual):
                    mark = "  " if want == got else "❌"
                    call = f"{op}({', '.join(map(repr, op_args))})"
                    print(f"   {mark} {call} 预期: {want} 实际: {got}")
        except Exception:
            print(f"Case {i+1}: 💥 ERROR | 操作: {ops}")
            print(traceback.format_exc())
    print(f"{'='*55}\n")


# =========================================================================
# 自动运行：脚本结束时，用主程序里的 tests 测试 Solution（或设计题的类）
# =========================================================================
@atexit.register
def _auto_run():
    main = sys.modules.get("__main__")
    solution_cls = getattr(main, "Solution", None)
    test_cases = getattr(main, "tests", None)
    if test_cases is None:
        return
    if solution_cls is not None:
        run_test_engine(solution_cls, test_cases)
    elif isinstance(test_cases, str) and parse_design_examples(test_cases):
        run_design_test_engine(main, test_cases)
