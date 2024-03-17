def cycle(i,visited,adj):
    if visited[i] : return True
    else :
        visited[i] = True
        res = False
        for u in adj[i]:
            res = res or cycle(u,visited,adj)
            if res : return True
        visited[i] = False
        return res