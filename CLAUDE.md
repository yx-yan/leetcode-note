# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
python test1.py                  # run the ad hoc test harness
python path/to/solution.py       # run a single solution file directly
python -m py_compile test1.py    # syntax check
```

No build step or test framework — validation is manual via `test1.py`.

## Solution Format

Every solution file follows this structure:

```python
# Problem: <title>
# Link: https://leetcode.com/problems/<slug>/
# Difficulty: Easy / Medium / Hard
# Topics: <tag1>, <tag2>

class Solution:
    def methodName(self, ...):
        pass

# Time:  O(?)
# Space: O(?)
# Notes: <key insight>
```

File naming: `id_slug.py` (e.g. `3660_jump_game_ix.py`). Older files use id-only names — keep existing names, use `id_slug.py` for new ones.

## Test Harness (`test1.py`)

Paste a `Solution` class into section 2, add test cases to `my_test_cases` in section 4, then run. The engine auto-detects the first method on `Solution`. Helper classes `ListNode`, `TreeNode`, and `Utils` (array ↔ linked list / tree conversions) are already defined there.

## After Adding a Solution

Update the progress table in `README.md` with the problem number, title (linked to the file), difficulty, and topics.
