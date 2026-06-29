class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建一个默认值为列表的字典，避免手动处理key不存在的情况
        anagram_map = defaultdict(list)
        
        for s in strs:
            # sorted(s)返回一个排好序的字符列表，例如['e', 'a', 't'] -> ['a', 'e', 't']
            # "".join(...)将其重新拼接为字符串"aet"作为字典的键
            sorted_key = "".join(sorted(s))

            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())