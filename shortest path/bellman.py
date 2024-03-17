edges = [
    (0,1,5),(0,3,7),(0,2,3),
    (1,3,3),(1,5,2),(2,3,1),
    (3,5,2),(1,0,5),(3,0,7),
    (2,0,3),(3,1,3),(5,1,2),
    (3,2,1),(5,3,2)
]
n=6
distance = [float('inf') for _ in range(n)]

source = 0
distance[source] = 0
for i in range(n-1):
    for edge in edges:
        a, b, w = edge 
        distance[b] = min(distance[b],distance[a]+w)

for i,item in enumerate(distance):
    print (i,item)