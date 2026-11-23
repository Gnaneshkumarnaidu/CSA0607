# TASK 5 – SAME GRAPH, DIFFERENT ALGORITHMIC REASONING (7 Marks)

### Task 5.1 – Greedy Shortest-Path Design (3 Marks)
Pseudocode for Dijkstra's Algorithm from source A:
```
ALGORITHM Dijkstra(Graph, Source)
INPUT:
  Graph: Adjacency list with non-negative edge weights
  Source: Starting vertex A
OUTPUT:
  Dist: Array of shortest path distances
  Prev: Array of predecessor vertices

BEGIN
  FOR EACH vertex v IN Graph.Vertices DO
    Dist[v] ← INFINITY
    Prev[v] ← NULL
    Visited[v] ← FALSE
  END FOR

  Dist[Source] ← 0

  WHILE there exists an unvisited vertex DO
    // Greedy selection of unvisited vertex with minimum tentative distance
    u ← UNVISITED vertex with MINIMUM Dist[u]
    IF Dist[u] = INFINITY THEN
      BREAK
    END IF
    Visited[u] ← TRUE

    // Relaxation of outgoing edges
    FOR EACH neighbor v OF u DO
      IF NOT Visited[v] THEN
        new_dist ← Dist[u] + Weight(u, v)
        IF new_dist < Dist[v] THEN
          Dist[v] ← new_dist
          Prev[v] ← u
        END IF
      END IF
    END FOR
  END WHILE

  RETURN Dist, Prev
END
```

### Task 5.2 – Change the Graph Assumption: Negative Edges (2 Marks)
- **Unsafe Assumption:** Dijkstra assumes that once a vertex is marked "Visited", its shortest path is permanently finalized. A negative weight edge encountered later can retroactively shorten the distance to an already-finalized vertex, invalidating Dijkstra's greedy invariant.
- **Bellman-Ford Repeated Relaxation Pseudocode:**
  ```
  FOR k ← 1 TO |V| - 1 DO
    FOR EACH directed edge (u, v) with weight w IN Edges DO
      IF Dist[u] != INFINITY AND Dist[u] + w < Dist[v] THEN
        Dist[v] ← Dist[u] + w
        Prev[v] ← u
      END IF
    END FOR
  END FOR
  ```
- **Detection of Negative Cycle:** Run one additional pass over all edges. If any edge can still be relaxed ($Dist[u] + w < Dist[v]$), then a reachable negative-weight cycle exists.

### Task 5.3 – Change Requirement: All-Pairs Shortest Paths (2 Marks)
- **Meaning of State $D^{(k)}[i][j]$:** Represents the shortest path distance from vertex $i$ to vertex $j$ considering only intermediate vertices from the subset $\{1, 2, \dots, k\}$.
- **Core State Transition (Floyd-Warshall):**
  ```
  FOR k ← 1 TO |V| DO
    FOR i ← 1 TO |V| DO
      FOR j ← 1 TO |V| DO
        D[i][j] ← MIN(D[i][j], D[i][k] + D[k][j])
      END FOR
    END FOR
  END FOR
  ```
- **Difference from Single-Source:** Single-source algorithms maintain a 1D vector of distances from a fixed source and grow paths outward, whereas Floyd-Warshall maintains an $n 	imes n$ matrix simultaneously considering all pairs and iteratively expands the allowed set of intermediate transit hubs.
