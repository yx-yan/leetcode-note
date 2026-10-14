# Problem: 3660. Jump Game IX
# Link: https://leetcode.com/problems/jump-game-ix/
# Difficulty: Medium
# Topics: Array, Stack, Union Find

# From index i you can:
#   jump forward to j > i  if nums[j] < nums[i]
#   jump backward to j < i if nums[j] > nums[i]
# Return an array where ans[i] = max value reachable from i.


class Solution:
    def maximumValueSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        # Key insight: if nums[i] > nums[j] for i < j, there is both a
        # forward edge i→j AND a backward edge j→i, forming a 2-cycle.
        # Transitivity makes all indices in an "inversion range" a single
        # connected component. Components are always contiguous intervals.
        #
        # Monotonic stack: maintain (max_val, start_idx) for each component.
        # When nums[i] < stack.top().max, merge current index with that
        # component (and keep merging leftward while the condition holds).
        # All indices in the same component share the component's max value.

        stack = []  # (max_val, start_idx)

        for i in range(n):
            curr_max = nums[i]
            start = i
            while stack and stack[-1][0] > nums[i]:
                prev_max, prev_start = stack.pop()
                curr_max = max(curr_max, prev_max)
                start = prev_start
            stack.append((curr_max, start))

        for k, (max_val, start) in enumerate(stack):
            end = stack[k + 1][1] if k + 1 < len(stack) else n
            for j in range(start, end):
                ans[j] = max_val

        return ans


# Time:  O(n)  — each index pushed/popped at most once
# Space: O(n)  — stack + output array
# Notes: Every forward edge i→j (nums[j] < nums[i]) implies a backward edge
#        j→i, so the directed graph is symmetric. SCCs = connected components,
#        which are contiguous intervals discoverable via a monotonic stack.
#        No inter-component edges exist between stack entries, so no additional
#        propagation is needed.
