class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 将数组转换为哈希集合，实现O(1)的查找，并自动去重
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            # 只有当 num - 1 不在集合中时，才说明num是一个新序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 顺着起点，依次查找连续的下一个数
                while current_num + 1 in num_set:
                    current_num +=1 
                    current_streak += 1
                
                # 更新最长连续序列的长度
                longest_streak = max(longest_streak, current_streak)

        return longest_streak