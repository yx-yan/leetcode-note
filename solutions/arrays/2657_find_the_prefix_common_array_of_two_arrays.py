# Problem: 2657. Find the Prefix Common Array of Two Arrays
# Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Difficulty: Medium
# Topics: Hash Table, Array

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        table = {}
        n = len(A)
        ans = 0
        output = []
        for i in range(n):
            if A[i] not in table:
                table[A[i]] = 1
            else:
                ans += 1
            if B[i] not in table:
                table[B[i]] = 1
            else:
                ans += 1
            output.append(ans)
        return output


# Time:  O(n)
# Space: O(n)
# Notes: Each value appears once in each input permutation. The running count
# increases when a value is encountered for the second time.
