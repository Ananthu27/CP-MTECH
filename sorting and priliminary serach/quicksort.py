def partition(ar,start,end):
    i = start-1
    p = end
    for j in range(start,end):
        if ar[j]<=ar[p]:
            i = i + 1
            ar[i],ar[j] = ar[j],ar[i]
    i = i + 1
    ar[i],ar[p] = ar[p],ar[i]
    return i

def quick(ar,start,end):
    if (end-start)>0:
        p = partition(ar,start,end)
        quick(ar,start,p-1)
        quick(ar,p+1,end)

ar = [5,1,7,3,4,2,8,2,1,1,3,5,2,4]
quick(ar,0,len(ar)-1)
print (ar)