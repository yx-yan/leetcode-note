# Problem: 2904. Shortest and Lexicographically Smallest Beautiful String
# Link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
# Difficulty: Medium
# Topics: String, Sliding Window


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left, right = 0, k - 1
        best_left, best_right = 0, 0
        one_positions = []
        for i in range(n):
            if s[i] == "1":
                one_positions.append(i)

        one_count = len(one_positions)
        if one_count < k:
            return ""
        best_span = 101
        while right < one_count:
            current_span = one_positions[right] - one_positions[left]
            if current_span == best_span:
                i = 0
                while (
                    i < k - 1
                    and one_positions[left + i] - one_positions[left]
                    == one_positions[best_left + i] - one_positions[best_left]
                ):
                    i += 1
                if (
                    one_positions[left + i] - one_positions[left]
                    > one_positions[best_left + i] - one_positions[best_left]
                ):
                    best_left = left
                    best_right = right
            if current_span < best_span:
                best_left = left
                best_right = right
                best_span = current_span
            right += 1
            left += 1

        return s[one_positions[best_left] : one_positions[best_right] + 1]


# Time:  O(nk) worst case because equal-length windows may compare k gaps
# Space: O(n)
# Notes: Collect the indices of every '1'. A beautiful substring with exactly
#        k ones corresponds to a window of k consecutive positions. Slide that
#        window to minimize its span; among ties, compare the gaps between ones
#        to keep the lexicographically smallest candidate.
