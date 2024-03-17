def algo1(input):
    best = 0
    for i in range(len(input)):
        for j in range(i,len(input)):
            sum = 0
            for k in range(i,j):
                sum = sum + input[k]
            best = max(best,sum)
    print (best)

def algo2(input):
    best = 0
    for i in range(len(input)):
        sum = 0
        for j in range(i,len(input)):
            sum = sum+input[j]
            best = max(best,sum)
    print (best)

def algo3(input):
    best = 0
    sum = 0
    for i in range(len(input)):
        sum = max(input[i],sum+input[i])
        best = max(best,sum)
    print (best)

input = [-1,2,4,-3,5,2,-5,2]
algo1(input)
algo2(input)
algo3(input)