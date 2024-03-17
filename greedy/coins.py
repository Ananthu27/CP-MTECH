def g_coin(coins,sum):
    # coins.sort()
    
    i = len(coins)-1
    sol = {}

    while(sum>0 and i<len(coins)):
        sol[i] = sum//coins[i]
        sum = sum - coins[i]*sol[i]
        i = i - 1
    
    for index in sol.keys():
        print (coins[index],'*',sol[index])

coins = [1, 5, 10, 50 ,100]
g_coin(coins,7779)