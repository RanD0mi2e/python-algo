import pytest
from src.utils.tree_node import TreeNode
from src.solutions.tree.kth_smallest_bst import Solution

def test_kth_smallest_bst():
    root = TreeNode.from_list([3,1,4,None,2])
    solution = Solution()
    assert solution.kthSmallest(root, 1) == 1