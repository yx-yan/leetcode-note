# LeetCode Note

个人 LeetCode Python 题解，按知识点分类。进度和打卡见 [study_plan.md](study_plan.md)。

## 目录

```text
leetcode-note/
├── study_plan.md        # 8 周打卡表（唯一的进度记录）
├── python_idioms.md     # Python 惯用法速查
├── solutions/           # 题解，按专题分目录，如 solutions/arrays/
├── template.py          # 新题解模板
├── playground.py        # 当前题目的临时调试区
├── test_solutions.py    # 已完成题目的回归测试
└── LeetCode_101.pdf     # 参考资料
```

## 每道题的流程

1. **想**：独立思考 15–20 分钟，卡住只看思路，不看代码。
2. **写**：在 `playground.py` 里写出能 AC 的版本。
3. **读**：精读 1–2 份高赞 Python 题解，新学到的写法记进 `python_idioms.md`。
4. **重写**：关掉题解，从零再写一遍。
5. **存档**：复制 `template.py` 到 `solutions/<专题>/<id>_<slug>.py`，
   在 `test_solutions.py` 补一个案例，然后在 `study_plan.md` 打卡。

```bash
python3 playground.py       # 调试当前题目
python3 test_solutions.py   # 测试已有题解
```
