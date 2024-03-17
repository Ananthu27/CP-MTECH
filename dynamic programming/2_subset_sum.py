def r(subset,sum,memo):
    try :
        return memo[(tuple(subset),sum)]
    except : 
        if not(len(subset)) and sum :
            memo[(tuple(subset),sum)] = False
            return memo[(tuple(subset),sum)]
        if not sum :
            memo[(tuple(subset),sum)] = True
            return memo[(tuple(subset),sum)]
        if subset[-1] <= sum :
            memo[(tuple(subset),sum)] = r(subset[:-1],sum-subset[-1],memo) or r(subset[:-1],sum,memo)
            return memo[(tuple(subset),sum)]
        else :
            memo[(tuple(subset),sum)] = r(subset[:-1],sum,memo)
            return memo[(tuple(subset),sum)]

# print(r([1,2,3,3,3,4,5,2,3,1,2,2,1,2,10],100,{}))
# print(r([3,34,4,12,5,2],9,{}))
# print(r([3,34,4,12,5,2],30,{}))