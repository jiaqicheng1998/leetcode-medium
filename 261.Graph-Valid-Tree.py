# You have a graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and a list of edges where edges[i] = 
# [ai, bi] indicates that there is an undirected edge between nodes 
# ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, 
# and false otherwise.

def validTree(n, edges):
    if len(edges) >= n:
        return False
    
    parent = [i for i in range(n)] # length equals the number of node, initialized to be the node itself
    rank = [1] * (n) # length equals the number of node, initialized to be an array of all ones
    connected = n # use a variable to count the connected components

    def find(node):
        p = parent[node]

        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1,n2):
        p1,p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2):
            return False
        else:
            connected -= 1
    return connected == 1