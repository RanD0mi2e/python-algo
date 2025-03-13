from src.solutions.two_sum import two_sum

def test_two_sum_basic():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_no_solution():
    nums = [1, 2, 3, 4]
    target = 10
    assert two_sum(nums, target) == []

def test_two_sum_duplicate_numbers():
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]