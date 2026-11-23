"""
Task 3: Routing Engine Under Changing Network Conditions
Dijkstra, Bellman-Ford, Negative Cycles, Floyd & Warshall
"""
import heapq

def dijkstra(graph, source, n):
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)]
    order = []
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        order.append(u)
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev, order

def bellman_ford(edges, n, source):
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                
    # Detect negative cycle
    has_neg_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_neg_cycle = True
            break
    return dist, prev, has_neg_cycle

def floyd_warshall(matrix, n):
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def warshall_reachability(adj_matrix, n):
    reach = [row[:] for row in adj_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

if __name__ == '__main__':
    # 8 vertices: 0 to 7. 12 edges.
    n = 8
    graph = {
        0: [(1, 4), (2, 3)],
        1: [(2, 2), (3, 5)],
        2: [(4, 7), (3, 1)],
        3: [(5, 2), (6, 6)],
        4: [(6, 1), (7, 4)],
        5: [(7, 3)],
        6: [(7, 2)],
        7: []
    }
    
    # Stage A: Dijkstra
    d_dist, d_prev, d_order = dijkstra(graph, 0, n)
    print("Stage A - Dijkstra on Non-negative Network (Source 0):")
    print(f"  Distances: {d_dist}")
    print(f"  Finalization Order: {d_order}")
    
    # Stage B: Negative Edge (introduce edge 2 -> 4 with weight -3)
    edges = []
    for u, neighbors in graph.items():
        for v, w in neighbors:
            edges.append((u, v, w))
    # Add negative edge
    edges_neg = [(u, v, -3 if (u==2 and v==4) else w) for u, v, w in edges]
    bf_dist, bf_prev, neg_cycle = bellman_ford(edges_neg, n, 0)
    print("\nStage B - Bellman-Ford with Negative Edge (2->4 wt -3):")
    print(f"  Bellman-Ford Distances: {bf_dist}")
    print(f"  Negative Cycle Detected: {neg_cycle}")
    
    # Stage C: Introduce Reachable Negative Cycle (5 -> 3 wt -5 forms cycle 3->5->3 with total wt -3)
    edges_neg_cycle = list(edges_neg)
    edges_neg_cycle.append((5, 3, -5))
    _, _, cycle_detected = bellman_ford(edges_neg_cycle, n, 0)
    print(f"\nStage C - Reachable Negative Cycle Detection: Detected = {cycle_detected}")
