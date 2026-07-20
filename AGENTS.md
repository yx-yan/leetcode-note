# Repository Guidelines

## Project Structure & Module Organization
This repository is a Python LeetCode notebook organized by topic. Problem solutions live in topic folders such as `arrays/`, `graphs/`, `stack_queue/`, and `two_pointers/`. Use one file per problem. Current naming is mixed: some files use the LeetCode id only (for example `two_pointers/2540.py`) and others use `id_slug.py` (for example `stack_queue/3660_jump_game_ix.py`). Prefer `id_slug.py` for new additions because it is easier to scan.

Shared references live at the repo root:
- `template.md`: starter header and `Solution` skeleton in Markdown form
- `test1.py`: local ad hoc test harness for running a solution method
- `README.md`: high-level project overview and progress table
- `LeetCode_101.pdf`: reference material

## Build, Test, and Development Commands
This project does not have a formal build step. Use Python directly from the repository root.

- `python test1.py`: run the local test harness and sample cases
- `python path\\to\\solution.py`: execute a problem file if it includes a runnable block
- `python -m py_compile test1.py`: quick syntax check for the harness or other modules

When adding a new problem, copy `template.md`, fill in the metadata header, then wire temporary cases into `test1.py` if needed.

## Coding Style & Naming Conventions
Use Python with 4-space indentation and keep solutions self-contained. Follow the existing pattern:
- `class Solution` with the LeetCode method name unchanged
- top-of-file metadata comments for problem, link, difficulty, and topics
- bottom summary comments for time, space, and key insight

Use `snake_case` for functions and variables, and keep comments short and algorithm-focused.

## Testing Guidelines
There is no dedicated `tests/` directory or coverage gate yet. Validate each solution with representative examples, edge cases, and at least one failing case before the fix. Keep temporary test data in `test1.py` small and readable.

## Commit & Pull Request Guidelines
Recent commits use short, imperative summaries such as `Added test script and textbook` and `Initial setup`. Keep commit messages concise and descriptive. For pull requests, include:
- what problems or folders changed
- why the approach was chosen if it is non-obvious
- sample inputs or output when behavior was validated locally
