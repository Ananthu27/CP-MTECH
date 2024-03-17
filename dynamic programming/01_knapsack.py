m = {}

def knapsack(profit,weight,w):
    try :
        return m[(tuple(profit),tuple(weight),w)]
    except :
        if not len(profit) or w==0 or not len(weight):
            m[(tuple(profit),tuple(weight),w)] = 0
            return m[(tuple(profit),tuple(weight),w)]
        elif weight[-1]<=w :
            m[(tuple(profit),tuple(weight),w)] = max(
                knapsack(profit[:-1],weight[:-1],w-weight[-1])+profit[-1],
                knapsack(profit[:-1],weight[:-1],w),
            )
            return m[(tuple(profit),tuple(weight),w)]
        else :
            m[(tuple(profit),tuple(weight),w)] = knapsack(profit[:-1],weight[:-1],w)
            return m[(tuple(profit),tuple(weight),w)]

sol = knapsack(
    [55,10,47,5,4,50,8,61,85,87],
    [95,4,60,32,23,72,80,62,65,46],
    269
)
print (sol)