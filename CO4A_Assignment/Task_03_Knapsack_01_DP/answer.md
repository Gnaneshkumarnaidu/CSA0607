# TASK 3 – FROM RECURRENCE TO EXECUTABLE LOGIC: 0/1 Knapsack (9 Marks)

### Task 3.1 – Define the State (1 Mark)
State $DP[i][w]$ represents the maximum total value achievable using a subset of the first $i$ items (from $\{1, 2, \dots, i\}$) such that the total weight does not exceed capacity $w$, where $0 \le i \le n$ and $0 \le w \le W$.

### Task 3.2 – Develop the Recurrence (2 Marks)
- **Base Conditions:**
  $DP[0][w] = 0$ for all $0 \le w \le W$ (0 items yield 0 value).
  $DP[i][0] = 0$ for all $0 \le i \le n$ (zero capacity holds zero value).
- **Recurrence Relation:**
  For item $i$ with weight $w_i$ and value $v_i$:
  $$DP[i][w] = \begin{cases} DP[i-1][w] & \text{if } w_i > w \\ \max(DP[i-1][w], \ DP[i-1][w - w_i] + v_i) & \text{if } w_i \le w \end{cases}$$
- **Explanation:**
  - If $w_i > w$, item $i$ physically exceeds available sub-capacity $w$, forcing exclusion.
  - If $w_i \le w$, we evaluate two subproblems: excluding item $i$ ($DP[i-1][w]$) versus including item $i$ ($DP[i-1][w-w_i] + v_i$). The optimal substructure guarantees that taking the maximum yields the global optimum for state $(i, w)$.

### Task 3.3 – Translate the Recurrence into Pseudocode (4 Marks)
```
ALGORITHM Knapsack01_DP(Weights, Values, n, W)
INPUT:
  Weights: Array of integers w[1..n]
  Values: Array of numbers v[1..n]
  n: Number of items
  W: Maximum knapsack capacity
OUTPUT:
  OptimumValue: Maximum achievable value
  SelectedItems: List of chosen item indices

BEGIN
  // Initialize table
  FOR w ← 0 TO W DO
    DP[0][w] ← 0
  END FOR

  FOR i ← 1 TO n DO
    DP[i][0] ← 0
    FOR w ← 1 TO W DO
      IF Weights[i] > w THEN
        DP[i][w] ← DP[i-1][w]
      ELSE
        DP[i][w] ← MAX(DP[i-1][w], DP[i-1][w - Weights[i]] + Values[i])
      END IF
    END FOR
  END FOR

  OptimumValue ← DP[n][W]

  // Reconstruct selected items
  SelectedItems ← EMPTY_LIST()
  curr_w ← W
  FOR i ← n DOWNTO 1 DO
    IF DP[i][curr_w] != DP[i-1][curr_w] THEN
      APPEND(SelectedItems, i)
      curr_w ← curr_w - Weights[i]
    END IF
  END FOR

  RETURN OptimumValue, SelectedItems
END
```

### Task 3.4 – Desk-Check (1 Mark)
Items: P(w=2, v=12), Q(w=3, v=20), R(w=4, v=25), S(w=5, v=30), Capacity $W=7$.
- $i=1$ (P, w=2, v=12): $w \ge 2 	o 12$.
- $i=2$ (Q, w=3, v=20): $w=3 	o 20; w=5 	o 12+20=32$.
- $i=3$ (R, w=4, v=25): $w=4 	o 25; w=6 	o 12+25=37; w=7 	o \max(32, 20+25)=45$.
- $i=4$ (S, w=5, v=30): $w=7 	o \max(DP[3][7], DP[3][2]+30) = \max(45, 12+30) = 45$.
- **Backtrack from (4, 7):**
  $DP[4][7] = DP[3][7] = 45 \implies$ S not included.
  $DP[3][7] (45) 
e DP[2][7] (32) \implies$ R included! New weight $= 7 - 4 = 3$.
  $DP[2][3] (20) 
e DP[1][3] (12) \implies$ Q included! New weight $= 3 - 3 = 0$.
- **Optimum Value:** 45. **Selected Items:** {Q, R} (Weights: 3+4=7, Values: 20+25=45).

### Task 3.5 – Explain the Dependency (1 Mark)
Each entry $DP[i][w]$ directly reads from the prior row: strictly $DP[i-1][w]$ and $DP[i-1][w - w_i]$. Because $w - w_i < w$, computing row $i$ requires that all subproblems in row $i-1$ for weights up to $w$ have already been finalized. This strict topological dependency dictates our bottom-up row-by-row iteration.
