# You have a graph of n nodes. You are given an integer n 
# and an array edges where edges[i] = [ai, bi] indicates 
# that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

def countComponents(n, edges):
    par = [i for i in range(n)]
    rank = [1] * n
    connected = n
    
    def find(n):
        p = par[n]

        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p
    
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if union(n1, n2):
            connected -= 1
    
    return connected
    