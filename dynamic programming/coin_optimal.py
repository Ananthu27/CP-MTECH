memo={}
memo[0] = 0
solution ={}
solution[0] = 0
from sys import maxsize


##################################################
##################################################

# FINDING THE MINIMUM NUMBER OF COINS REQUIRED
def coin(value,coins) :
    # indentify the bound after which we need to return maxvalue for minimization
    # and minvalue for maximization as this path is to be neglected as not found feasible. 
    if value < 0 :
        return maxsize
    try :
        return memo[value]
    except : 
        # initially findout whether the objective function optimization is minimizatio or maximization.
        memo[value] = min(
            [(coin(value-denomination,coins)+1) for denomination in coins]
        )
        return memo[value]

D = {1,3,4}
# [print (coin(i,D)) for i in range (10+1)]
# print (memo)

##################################################
##################################################

# FINDING THE EXACT SOLUITON
def coin_sol(value,coins) :
    if value < 0 :
        return maxsize
    try : 
        return memo[value]
    except : 
        memo[value] = maxsize
        for denomination in coins:
            if value-denomination>=0 and memo[value] > coin_sol(value-denomination,coins)+1 :
                memo[value] = coin_sol(value-denomination,coins)+1
                solution[value] = denomination
        return memo[value]

# [print (coin_sol(n,D)) for n in range(10+1)]

# METHOD TO PRINT THE SOLUTION WITH MINIMUM COINS
def print_solution (n):
    coin_sol(n)
    while (n>0):
        print (solution[n])
        n = n-solution[n]

##################################################
##################################################

# TOATL NUMBER OF POSSIBLE SOLUTIONS
nums = {}
nums[0] = 1

def coins_nums(value,coins):
    if value < 0 : 
        return 0
    try : 
        return nums[value]
    except :
        nums[value] = sum([coins_nums(value-n,coins) for n in coins])
        return nums[value]

[print (coins_nums(n,D)) for n in range (10+1)]