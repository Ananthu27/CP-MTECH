# 1. Fibonacci Sequence
def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr

# 2. Binomial Coefficient (n choose k)
def binomial_coefficient_iterative(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n][k]

# 3. Longest Common Subsequence
def lcs_iterative(X, Y, m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# 4. Knapsack Problem
def knapsack_iterative(W, wt, val, n):
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

# Test the iterative solutions
print(f"Fibonacci(6): {fibonacci_iterative(6)}")
print(f"Binomial Coefficient(5, 2): {binomial_coefficient_iterative(5, 2)}")
X = "AGGTAB"
Y = "GXTXAYB"
print(f"Longest Common Subsequence: {lcs_iterative(X, Y, len(X), len(Y))}")
W = 10
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
print(f"Knapsack Value: {knapsack_iterative(W, wt, val, len(wt))}")