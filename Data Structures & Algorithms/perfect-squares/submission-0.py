class Solution:
    def numSquares(self, n: int) -> int:
        # Generate all perfect squares <= n
        lst = []
        i = 1
        while i*i <= n:
            lst.append(i*i)
            i += 1

        # dp[total] = min number of perfect squares to sum to total
        dp = {0: 0}

        for total in range(1, n+1):
            dp[total] = float("inf")
            for sq in lst:
                if total - sq >= 0:
                    dp[total] = min(dp[total], 1 + dp[total - sq])

        return dp[n]
