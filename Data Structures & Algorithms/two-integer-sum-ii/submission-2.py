class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i , j = 0 , len(numbers) - 1
        i = 0
        index = 0
        
        while index < len(numbers):
            j = len(numbers) - 1
            num = target - numbers[index]

            while j > index:
                if numbers[j] == num:
                    return [index + 1 , j + 1]
                else:
                    j -= 1
            
            index += 1
