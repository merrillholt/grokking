def knapSack(W, wt, val, n):
    # Create a 2D array to store the maximum value at each n and W
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Example usage
profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)
print(knapSack(W, weight, profit, n))