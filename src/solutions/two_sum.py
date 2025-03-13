from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    LeetCode 1: Two Sum
    给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
    
    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    返回 [0, 1]
    因为 nums[0] + nums[1] = 2 + 7 = 9
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []  # 如果没有找到解

# if __name__ == "__main__":
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = two_sum(nums, target)
#     print(result)