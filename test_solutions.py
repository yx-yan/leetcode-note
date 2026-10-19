import importlib.util
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def load_solution(relative_path: str):
    """Load a solution whose filename starts with a problem number."""
    path = PROJECT_ROOT / relative_path
    module_name = "solution_" + path.stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load solution from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SolutionTests(unittest.TestCase):
    def test_1_two_sum(self):
        module = load_solution("solutions/arrays/1_two_sum.py")

        for solution_cls in (module.SolutionBruteForce, module.SolutionHashMap):
            solution = solution_cls()
            self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])
            self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])
            self.assertEqual(solution.twoSum([3, 3], 6), [0, 1])

    def test_49_group_anagrams(self):
        module = load_solution("solutions/arrays/49_group_anagrams.py")

        def normalize(groups):
            # 组的顺序、组内顺序都不重要
            return sorted(sorted(g) for g in groups)

        for solution_cls in (module.SolutionSort, module.SolutionCount):
            solution = solution_cls()
            self.assertEqual(
                normalize(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
                normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
            )
            self.assertEqual(solution.groupAnagrams([""]), [[""]])
            self.assertEqual(solution.groupAnagrams(["a"]), [["a"]])

    def test_128_longest_consecutive(self):
        module = load_solution("solutions/arrays/128_longest_consecutive_sequence.py")

        for solution_cls in (
            module.SolutionSort,
            module.SolutionHashSet,
            module.SolutionBoundary,
            module.SolutionUnionFind,
        ):
            solution = solution_cls()
            self.assertEqual(solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
            self.assertEqual(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
            self.assertEqual(solution.longestConsecutive([1, 0, 1, 2]), 3)
            self.assertEqual(solution.longestConsecutive([]), 0)
            self.assertEqual(solution.longestConsecutive([-3, -2, -1, 5]), 3)

    def test_217_contains_duplicate(self):
        module = load_solution("solutions/arrays/217_contains_duplicate.py")

        for solution_cls in (
            module.SolutionHashSet,
            module.SolutionOneLiner,
            module.SolutionSort,
        ):
            solution = solution_cls()
            self.assertTrue(solution.containsDuplicate([1, 2, 3, 1]))
            self.assertFalse(solution.containsDuplicate([1, 2, 3, 4]))
            self.assertTrue(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_238_product_except_self(self):
        module = load_solution("solutions/arrays/238_product_of_array_except_self.py")

        for solution_cls in (
            module.SolutionTwoArrays,
            module.SolutionConstantSpace,
        ):
            solution = solution_cls()
            self.assertEqual(solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
            self.assertEqual(solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
            self.assertEqual(solution.productExceptSelf([0, 0]), [0, 0])
            self.assertEqual(solution.productExceptSelf([2, 3]), [3, 2])

    def test_242_valid_anagram(self):
        module = load_solution("solutions/arrays/242_valid_anagram.py")

        for solution_cls in (
            module.SolutionCount,
            module.SolutionSort,
            module.SolutionHashMap,
            module.SolutionCounter,
            module.SolutionArray,
        ):
            solution = solution_cls()
            self.assertTrue(solution.isAnagram("anagram", "nagaram"))
            self.assertFalse(solution.isAnagram("rat", "car"))
            self.assertFalse(solution.isAnagram("ab", "a"))
            self.assertFalse(solution.isAnagram("aab", "abb"))

    def test_303_range_sum_query(self):
        module = load_solution("solutions/arrays/303_range_sum_query_immutable.py")

        for cls in (
            module.NumArrayBruteForce,
            module.NumArrayPrefixSum,
            module.NumArrayAccumulate,
        ):
            obj = cls([-2, 0, 3, -5, 2, -1])
            self.assertEqual(obj.sumRange(0, 2), 1)
            self.assertEqual(obj.sumRange(2, 5), -1)
            self.assertEqual(obj.sumRange(0, 5), -3)
            self.assertEqual(obj.sumRange(3, 3), -5)

    def test_347_top_k_frequent(self):
        module = load_solution("solutions/arrays/347_top_k_frequent_elements.py")

        for solution_cls in (
            module.SolutionSort,
            module.SolutionCounter,
            module.SolutionBucket,
        ):
            solution = solution_cls()
            # 答案顺序不重要
            self.assertEqual(sorted(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
            self.assertEqual(solution.topKFrequent([1], 1), [1])
            self.assertEqual(
                sorted(solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)), [1, 2]
            )

    def test_2196_create_binary_tree(self):
        module = load_solution("solutions/trees/2196_create_binary_tree_from_descriptions.py")
        descriptions = [
            [20, 15, 1],
            [20, 17, 0],
            [50, 20, 1],
            [50, 80, 0],
            [80, 19, 1],
        ]

        root = module.Solution().createBinaryTree(descriptions)

        self.assertEqual(root.val, 50)
        self.assertEqual((root.left.val, root.right.val), (20, 80))
        self.assertEqual((root.left.left.val, root.left.right.val), (15, 17))
        self.assertEqual(root.right.left.val, 19)

    def test_2540_minimum_common_value(self):
        module = load_solution("solutions/two_pointers/2540_minimum_common_value.py")
        solution = module.Solution()

        self.assertEqual(solution.getCommon([1, 2, 3], [2, 4]), 2)
        self.assertEqual(solution.getCommon([1, 2], [3, 4]), -1)

    def test_2657_prefix_common_array(self):
        module = load_solution(
            "solutions/arrays/2657_find_the_prefix_common_array_of_two_arrays.py"
        )
        solution = module.Solution()

        self.assertEqual(
            solution.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]),
            [0, 2, 3, 4],
        )

    def test_2904_shortest_beautiful_substring(self):
        module = load_solution(
            "solutions/sliding_window/2904_shortest_and_lexicographically_smallest_beautiful_string.py"
        )
        solution = module.Solution()

        self.assertEqual(solution.shortestBeautifulSubstring("100011001", 3), "11001")
        self.assertEqual(solution.shortestBeautifulSubstring("1011", 2), "11")
        self.assertEqual(solution.shortestBeautifulSubstring("000", 1), "")

    def test_3043_longest_common_prefix(self):
        module = load_solution(
            "solutions/arrays/3043_find_the_length_of_the_longest_common_prefix.py"
        )
        solution = module.Solution()

        self.assertEqual(solution.longestCommonPrefix([1, 10, 100], [1000]), 3)
        self.assertEqual(solution.longestCommonPrefix([1, 2, 3], [4, 4, 4]), 0)

    def test_3660_jump_game_ix(self):
        module = load_solution("solutions/stack_queue/3660_jump_game_ix.py")
        solution = module.Solution()

        self.assertEqual(solution.maximumValueSum([2, 1, 3]), [2, 2, 3])
        self.assertEqual(solution.maximumValueSum([4, 3, 2, 1]), [4, 4, 4, 4])
        self.assertEqual(solution.maximumValueSum([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
