class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        dicto = Counter(nums)
        sorted_dict = sorted(dicto, key=lambda x:dicto[x], reverse=True)
        return list(sorted_dict)[:k]
