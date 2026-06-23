class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index = 0
        
        # while index < len(numbers):
        #     j = len(numbers) - 1
        #     num = target - numbers[index]

        #     while j > index:
        #         if numbers[j] == num:
        #             return [index + 1 , j + 1]
        #         else:
        #             j -= 1
            
        #     index += 1


        i , j = 0 , len(numbers) - 1

        while i < j:
            val = numbers[i] + numbers[j]

            if val > target:
                j -= 1

            elif val < target:
                i += 1

            elif val == target:
                return [i + 1 , j + 1]
