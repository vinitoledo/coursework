class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(i)
            for j in range(len(nums)-1,i,-1):
                if i ==j:
                    pass
                if nums[i] + nums[j] == target:
                    return [i,j]
        