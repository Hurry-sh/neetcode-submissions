class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

# Solution 1 [O(m*logn)]

        # for i in matrix:
        #     if target >= i[0] and target <= i[len(i) - 1]:
        #         l, r = 0, len(i)-1
        #         while l <= r:
                    # m = l + ((r - l) // 2)
                    # if target < i[m]:
                    #     r = m - 1
                    # elif target > i[m]:
                    #     l = m + 1
                    # else:
                    #     return True
        # return False

# Solution 2 [O(logmn)]

        l_out, r_out = 0, len(matrix) - 1

        while l_out <= r_out:
            m_out = l_out + ((r_out - l_out) // 2)
            if target < matrix[m_out][0]:
                r_out = m_out - 1
            elif target > matrix[m_out][len(matrix[m_out])-1]:
                l_out = m_out + 1
            else:
                l, r = 0, len(matrix[m_out])-1
                while l <= r:
                    m = l + ((r - l) // 2)
                    if target < matrix[m_out][m]:
                        r = m - 1
                    elif target > matrix[m_out][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False




        