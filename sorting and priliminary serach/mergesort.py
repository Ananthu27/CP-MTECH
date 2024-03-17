def merge(ar,s1,e1,s2,e2):
    res = []
    i,j = s1,s2
    while (i<=e1 and j<=e2):
        if ar[i]<ar[j]:
            res.append(ar[i])
            i = i + 1
        else :
            res.append(ar[j])
            j = j + 1
    while (i<=e1) : 
        res.append(ar[i])
        i = i + 1
    while (j<=e2) :
        res.append(ar[j])
        j = j + 1
    for i in range(s1,e2+1):
        ar[i] = res.pop(0)

def sort(ar,start,end):
    if start<end:
        mid = (end+start)//2
        sort(ar,start,mid)
        sort(ar,mid+1,end)
        merge(ar,start,mid,mid+1,end)

ar = [1,3,4,8,1,2,2,7,2,3,7,1,3,2,-5,-7]
sort(ar,0,len(ar)-1)
print (ar)