# Problem: 238. Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Topics: Array, Prefix Sum

from typing import List


# =========================================================================
# 方法一：左积数组 + 右积数组
# =========================================================================
class SolutionTwoArrays:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n   # left[i]：i 左边所有数的乘积（不含自己）
        right = [1] * n  # right[i]：i 右边所有数的乘积（不含自己）
        output = [0] * n
        product_l = 1
        product_r = 1
        for i in range(1, n):  # 一次循环同时填左积（正着）和右积（倒着）
            product_l *= nums[i - 1]
            product_r *= nums[n - i]
            left[i] = product_l
            right[n - i - 1] = product_r

        for i in range(n):
            output[i] = left[i] * right[i]
        return output

# Time:  O(n)
# Space: O(n)，left 和 right 两个辅助数组


# =========================================================================
# 方法二：output 先存左积，再用一个变量倒着乘上右积（O(1) 额外空间）
# =========================================================================
class SolutionConstantSpace:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        for i in range(1, n):  # 第一遍 →：output[i] 只存左积
            output[i] = output[i - 1] * nums[i - 1]

        product_r = 1
        for i in range(n - 1, -1, -1):  # 第二遍 ←：边走边乘右积
            output[i] *= product_r  # 先用（此时还不含 nums[i]）
            product_r *= nums[i]    # 再把自己乘进去，留给左边的数
        return output

# Time:  O(n)
# Space: O(1)，输出数组不算额外空间


Solution = SolutionConstantSpace

# Notes: answer[i] = i 左边的乘积 × i 右边的乘积，正反各扫一遍，完全不用除法。
#        先全乘再除的坑：遇到 0 会 ZeroDivisionError，`/` 还会返回浮点数，
#        而且题目明确禁止除法。
#        我写的时候的坑：left[i] 存成了"含自己"的前缀积，只好用
#        left[i - 1] * right[i + 1]，结果 i = n - 1 越界，
#        i = 0 时 left[-1] 取到最后一个元素悄悄算错。
#        改成"不含自己"（left[0] = 1）后直接 left[i] * right[i]，没有边界问题。
#        进阶：右积数组用一个变量代替，左积直接写进 output。
# Python: [1] * n 先占好位置再按下标填，比每次 insert(0, x)（O(n)）快；
#         range(n - 1, -1, -1) 从 n - 1 倒着数到 0（终点 -1 取不到）
