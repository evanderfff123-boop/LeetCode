class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建哈希表，用于存储 {数值: 下标}
        hash_map = {}

        # 使用 enumerate 可以同时拿到下标 i 和对应的数值 num
        for i, num in enumerate(nums):
            complement = target - num
            # 检查配对的数是否已经在哈希表中
            if complement in hash_map:
                # 如果在，返回配对数的下标和当前数的下标
                return [hash_map[complement], i]
            # 如果不在，将当前数和下标存入哈希表
            hash_map[num] = i
        return []