# TASK 3 – ROUTING ENGINE UNDER CHANGING NETWORK CONDITIONS (10 Marks)

### Stage A – Normal Routing: Dijkstra's Algorithm
- Network with 8 vertices (0 to 7) and 12 edges.
- Dijkstra from Source 0:
  - Distances: `[0, 4, 3, 4, 10, 6, 8, 9]`
  - Order of finalization: `[0, 2, 1, 3, 5, 6, 7, 4]`

### Stage B – Introduce a Negative Edge
- **Modification:** Change edge $2 	o 4$ weight from $+7$ to $-3$.
- **Prediction:** Dijkstra will fail because vertex 2 is popped early and neighbor 4 is relaxed, but any subsequent negative updates cannot propagate backwards once marked visited.
- **Bellman-Ford Execution:** Bellman-Ford performs repeated passes and correctly finds distance to 4 is $3 + (-3) = 0$, and to 7 is $0 + 4 = 4$, beating Dijkstra's faulty assumption.

### Stage C – Production Failure: Reachable Negative Cycle
- **Modification:** Add directed edge $5 	o 3$ with weight $-5$.
- Path $3 	o 5$ has cost 2; edge $5 	o 3$ has cost $-5$. Cycle sum $= 2 - 5 = -3 < 0$.
- **Detection Mechanism:** On the $|V|$-th relaxation pass, edge $5 	o 3$ continues to relax $Dist[3] \leftarrow Dist[5] - 5$. The algorithm detects this violation and aborts, raising a `NegativeCycleException`.

### Stage D – Change the Requirement: Floyd & Warshall Matrices
- Implemented $O(V^3)$ Floyd-Warshall all-pairs shortest path matrix and Warshall transitive closure reachability bitmask matrix. Both matrices fully displayed in report.
