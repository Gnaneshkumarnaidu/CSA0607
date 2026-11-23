"""
Task 5: Three Greedy Engineers, One Network
Kruskal + Prim + Boruvka on the same connected weighted graph
"""
import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal(n, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    tot_cost = 0
    for u, v, w in sorted_edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            tot_cost += w
            if len(mst) == n - 1:
                break
    return tot_cost, mst

def prim(n, graph):
    visited = [False] * n
    mst = []
    tot_cost = 0
    pq = [(0, 0, -1)] # (weight, curr_vertex, parent)
    while pq and len(mst) < n:
        w, u, p = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if p != -1:
            mst.append((p, u, w))
            tot_cost += w
        for v, weight in graph.get(u, []):
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))
    return tot_cost, mst

if __name__ == '__main__':
    n = 6
    edges = [
        (0, 1, 4), (0, 2, 4), (1, 2, 2),
        (1, 3, 5), (2, 3, 5), (2, 4, 9),
        (3, 4, 7), (3, 5, 3), (4, 5, 4)
    ]
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
        
    k_cost, k_mst = kruskal(n, edges)
    p_cost, p_mst = prim(n, graph)
    print("MST Comparison:")
    print(f"  Kruskal Total Cost: {k_cost}, Edges: {k_mst}")
    print(f"  Prim Total Cost: {p_cost}, Edges: {p_mst}")
