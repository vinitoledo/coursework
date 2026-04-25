class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        all_groups = {}
        for word in strs:
            ordered = tuple(sorted(word))
            all_groups[ordered] = all_groups.get(ordered,[]) + [word]

        return [i for i in all_groups.values()]