# TASK 5 – THREE GREEDY ENGINEERS, ONE NETWORK: Kruskal + Prim + Borůvka (7 Marks)

### Comparison of Greedy Mechanics
1. **Kruskal's Algorithm:**
   - **Safe Edge:** Globally lightest edge in the entire network that does not create a cycle.
   - **Data Structure:** Disjoint-set union-find with path compression ($O(E \log E)$).
   - **Growth:** A distributed forest of trees that merges into a single tree.
2. **Prim's Algorithm:**
   - **Safe Edge:** Lightest edge connecting a vertex in the currently grown tree to an external vertex.
   - **Data Structure:** Priority queue / Min-heap ($O(E \log V)$).
   - **Growth:** A single tree growing outward from an arbitrary start node.
3. **Borůvka's Algorithm:**
   - **Safe Edge:** Simultaneously finds the cheapest incident edge for every connected component.
   - **Data Structure:** Component indexing and contractive phases ($O(E \log V)$).
   - **Growth:** Parallel multi-fragment growth.

### Stress the Design: Multiple Equivalent MSTs
- **Observation:** When multiple edges share identical minimal weights, Kruskal, Prim, and Borůvka may select different subsets of edges depending on tie-breaking orders, yet all produce identical minimum total weight (cut-property invariant).

### Industry Deployment Analysis
- **Sparse Network ($E pprox V$):** Kruskal's algorithm is optimal due to quick edge sorting and lightweight disjoint sets.
- **Dense Network ($E pprox V^2$):** Prim's algorithm with an adjacency matrix or Fibonacci heap ($O(V^2)$) outperforms Kruskal.
- **Distributed / Parallel Cloud Resources:** Borůvka's algorithm is far superior because each component independently identifies its minimum-weight edge without global locks.
