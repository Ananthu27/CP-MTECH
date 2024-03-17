adj = {}
adj[1] = [2,4]
adj[2] = [1,3,5]
adj[3] = [2,5]
adj[4] = [1]
adj[5] = [2,3]

visited = {}
for vertex in adj:
    visited[vertex] = False
distance = {}

source = 1
distance[source] = 0
visited[source] = True
queue = [source]

while (len(queue)):
    v = queue.pop(0)
    for u in adj[v]:
        if visited[u]: continue
        visited[u] = True
        print('@',u)
        distance[u] = distance[v] + 1
        queue.append(u)

for vertex in distance:
    print (vertex,distance[vertex])