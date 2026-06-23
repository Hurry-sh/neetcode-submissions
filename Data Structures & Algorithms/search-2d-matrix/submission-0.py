class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in matrix:
            if target >= i[0] and target <= i[len(i) - 1]:
                l, r = 0, len(i)-1
                while l <= r:
                    m = l + ((r - l) // 2)

                    if target < i[m]:
                        r = m - 1
                    elif target > i[m]:
                        l = m + 1
                    else:
                        return True

        return False


        