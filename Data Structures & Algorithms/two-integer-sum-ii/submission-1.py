class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        e = len(numbers) -1

        while i < e:
            check = numbers[i] + numbers[e]

            if check == target:
                return[i+1,e+1]
            if check > target:
                e -=1 
            else:
                i+= 1