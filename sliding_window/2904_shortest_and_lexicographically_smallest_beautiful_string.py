# Problem: Shortest and Lexicographically Smallest Beautiful String
# Link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
# Difficulty: Medium
# Topics: String, Sliding Window

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l, r = 0, k - 1
        ld, rd = 0, 0
        n1 = []
        for i in range(n):
            if s[i] == "1":
                n1.append(i)

        m = len(n1)
        if m < k:
            return ""
        le = 101
        while r < m:
            if n1[r] - n1[l] == le:
                i = 0
                while n1[l + i] - n1[l] == n1[ld + i] - n1[ld] and i < k - 1:
                    i += 1
                if n1[l + i] - n1[l] > n1[ld + i] - n1[ld]:
                    ld = l
                    rd = r
            if n1[r] - n1[l] < le:
                ld = l
                rd = r
                le = n1[r] - n1[l]
            r += 1
            l += 1

        return s[n1[ld]:n1[rd] + 1]

# Time:  O(n)
# Space: O(n)
# Notes: Collect indices of every '1' in n1. A beautiful substring with exactly
#        k ones corresponds to a window of k consecutive indices in n1; its
#        length is n1[r] - n1[l] + 1. Slide this window across n1 to find the
#        minimum length, then among ties compare the "1" run pattern (gaps
#        between consecutive ones) to keep the lexicographically smallest
#        candidate.
