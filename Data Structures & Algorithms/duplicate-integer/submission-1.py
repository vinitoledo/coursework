class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_contaiend = set()

        for n in nums:
            if n in numbers_contaiend:
                return True
            
            numbers_contaiend.add(n)
        
        return False