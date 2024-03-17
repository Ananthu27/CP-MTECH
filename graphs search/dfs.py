adj = {}
adj[1] = [2, 4]
adj[2] = [1, 3, 5]
adj[3] = [2, 5]
adj[4] = [1]
adj[5] = [2, 3]

def dfs(v, visited):
    if visited[v]:
        return
    else:
        visited[v] = True
        print('@', v)
        for u in adj[v]:
            dfs(u, visited)

visited = {}
for vertex in adj.keys():
    visited[vertex] = False

source_vertex = 1
dfs(source_vertex, visited)