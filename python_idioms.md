# Python 刷题惯用法速查

读题解时遇到不认识的写法就加到这里，并注明出处题号。下面先列出打卡表会用到的高频写法。

## 容器与 collections

| 写法 | 作用 | 出处 |
|---|---|---|
| `seen = {}` / `seen.get(x, 0)` | 哈希表查找，带默认值 | 1 |
| `count[c] = count.get(c, 0) + 1` | 手写计数，key 不存在时从 0 开始 | 242 |
| `if x in seen:` | 判断 key 是否在 dict 里，平均 O(1)；list 的 `in` 是 O(n) | 1 |
| `seen[num] = i` | 存「值 → 下标」，之后按值反查下标 | 1 |
| 边遍历边存：先查 `target - num`，再存 `num` | 一遍扫描找配对；先查后存，避免同一个元素用两次 | 1 |
| `seen = set()` / `seen.add(x)` | 只判断「是否出现过」用 set；需要计数或存下标才用 dict | 217 |
| `len(set(nums)) != len(nums)` | 一行判断有无重复，但不能提前退出 | 217 |
| `Counter(s)` | 计数；两个 Counter 可以直接 `==` 比较 | 242 |
| `defaultdict(list)` | 访问不存在的 key 时自动建空列表 | 49 |
| `groups[tuple(count)]` | dict 的 key 必须可哈希：list 不行，转成 tuple 或 str | 49 |
| `deque()` / `popleft()` | O(1) 队首出队，用于 BFS | 102 |
| `OrderedDict` / `move_to_end` | 有序字典，LRU 缓存 | 146 |

## heapq 与 bisect

| 写法 | 作用 | 出处 |
|---|---|---|
| `heapq.heappush(h, x)` / `heappop(h)` | 小顶堆；大顶堆存 `-x` | 703 |
| `heapq.heappush(h, (key, i, obj))` | 元组按 key 排序，`i` 避免比较 obj | 23 |
| `bisect_left(a, x)` | 第一个 `>= x` 的位置 | 35 |
| `bisect_right(a, x)` | 第一个 `> x` 的位置 | 34 |

## 循环与解包

| 写法 | 作用 | 出处 |
|---|---|---|
| `for i, x in enumerate(nums)` | 同时拿下标和值 | 1 |
| `any(x == y for ...)` | 生成器 + `any`，遇到 True 就短路返回 | 217 |
| `for a, b in zip(s, t)` | 并行遍历 | 242 |
| `ord(c) - ord('a')` | 小写字母映射到 0-25，配合 `[0] * 26` 计数 | 242 |
| `a, b = b, a` | 交换，右边先整体求值 | 283 |
| `q, r = divmod(x, 10)` | 同时取商和余数 | 2 |
| `for _ in range(len(q))` | BFS 按层处理 | 102 |

## 函数与递归

| 写法 | 作用 | 出处 |
|---|---|---|
| `@cache`（`from functools import cache`） | 记忆化递归 | 70 |
| `nonlocal ans` | 内部函数修改外层变量 | 543 |
| `res.append(path[:])` | 存路径的拷贝，而不是引用 | 78 |

## 常见坑

| 写法 | 问题 | 出处 |
|---|---|---|
| `[[0] * n] * m` | m 行是同一个列表；应写 `[[0] * n for _ in range(m)]` | 62 |
| `a // b`（负数） | 向下取整；向零取整用 `int(a / b)` | 150 |
| `float('inf')` | 初始化最小值；最大值用 `float('-inf')` | 121 |
| 循环里调用 `s.count(c)` | 每次都扫整个字符串，整体变 O(n²)；先一次遍历数完 | 242 |
