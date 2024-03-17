# 1. Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Your iterative Fibonacci solution here

# 2. Binomial Coefficient (n choose k)
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

# Your iterative binomial coefficient solution here

# 3. Longest Common Subsequence
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

# Your iterative LCS solution here

# 4. Knapsack Problem
def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1),
                   knapsack(W, wt, val, n-1))

# Your iterative knapsack solution here
