# COMPREHENSIVE TECHNICAL ASSIGNMENT REPORT
## CSA06 — Design and Analysis of Algorithms (DAA)
### Course Outcome 4 (CO4): Algorithmic Design Through Pseudocode (Part I)

---

<div align="center">

# SIMATS ENGINEERING
### DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING

---

**Course Code & Title:** CSA0606 — Design and Analysis of Algorithms  
**Assessment:** Assignment 4A — Course Outcome 4 (CO4 - Part I)  
**Maximum Marks:** 50  
**Mode:** Individual Technical Assignment  
**Student Name:** M.Gnanesh kumar naidu  
**Registration Number:** 192371051  
**Academic Year:** 2024–2025 (Third Year / B.E. CSE)  
**Standard Followed:** SIMATS Engineering — Handbook for Algorithmic Pseudocode  
**Source Document:** [Original Assessment Guidelines](Report/Reference/ORIGINAL_STUDENT_REFERENCE%20-%20CO4A%20ASSIGNMENT.pdf)

</div>

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement & Algorithmic Progression](#2-problem-statement--algorithmic-progression)
3. [SIMATS Engineering Pseudocode Standards](#3-simats-engineering-pseudocode-standards)
4. [Complete Task Solutions & Forensic Analyses](#4-complete-task-solutions--forensic-analyses)
   - [Task 1 – Algorithm Design Review: Diagnose & Repair Informal Pseudocode](#task-1--algorithm-design-review-diagnose-and-repair-poor-pseudocode-6-marks)
   - [Task 2 – From Business Requirement to Greedy Pseudocode: Job Sequencing with Deadlines](#task-2--from-business-requirement-to-greedy-pseudocode-job-sequencing-with-deadlines-8-marks)
   - [Task 3 – From Recurrence to Executable Logic: 0/1 Knapsack Dynamic Programming](#task-3--from-recurrence-to-executable-logic-01-knapsack-9-marks)
   - [Task 4 – Pseudocode Forensics: Defect Isolation & WordBreak Repair](#task-4--pseudocode-forensics-find-explain-and-repair-an-algorithmic-defect-7-marks)
   - [Task 5 – Same Graph, Different Algorithmic Reasoning: Dijkstra, Bellman-Ford, and Floyd](#task-5--same-graph-different-algorithmic-reasoning-7-marks)
   - [Task 6 – Day-4 Design Challenge: Energy-Aware Job Scheduling in Cloud Data Centres](#task-6--design-challenge-energy-aware-job-scheduling-in-a-cloud-data-centre-13-marks)
5. [Comparative Analysis of Greedy vs Dynamic Programming](#5-comparative-analysis-of-greedy-vs-dynamic-programming)
6. [Adversarial Testing & Boundary Verification](#6-adversarial-testing--boundary-verification)
7. [Conclusion & Technical Reflection](#7-conclusion--technical-reflection)
8. [References](#8-references)

---

## 1. Executive Summary

This report establishes complete algorithmic designs for optimization problems under the curriculum of Course Outcome 4 (CO4) for CSA0606. Emphasizing design-before-implementation, all solutions follow the canonical progression:
$$\text{Interpret} \longrightarrow \text{Identify Decision/State} \longrightarrow \text{Design Logic} \longrightarrow \text{Write Pseudocode} \longrightarrow \text{Trace} \longrightarrow \text{Challenge} \longrightarrow \text{Refine}$$

Across six extensive tasks, this submission provides:
1. **Defect Diagnosis:** Isolating five fatal deficiencies in an informal vehicle-loading algorithm and engineering a robust fractional greedy design.
2. **Greedy Scheduling:** Transforming a cloud revenue model with deadlines into an optimal slot-allocation strategy with complete step-by-step desk checks.
3. **Dynamic Programming Synthesis:** Deriving the optimal substructure recurrence for 0/1 knapsack, designing a 2D bottom-up tabular solver, and proving backtrack reconstruction correctness.
4. **Algorithmic Forensics:** Diagnosing a critical subproblem independence flaw in a dynamic programming string segmenter (`WordBreak`) and applying minimal repair logic.
5. **Graph Transition Under Stress:** Demonstrating how negative edge insertions destroy Dijkstra's greedy invariant, formulating Bellman-Ford cycle detection, and specifying Floyd-Warshall all-pairs transitions.
6. **Energy-Aware Design Challenge:** Solving an unguided cloud data center energy-saving challenge via Weighted Interval Scheduling ($O(n \log n)$) and validating resilience against adversarial inputs.

---

## 2. Problem Statement & Algorithmic Progression

Modern cloud and logistics platforms demand algorithms capable of provable correctness and efficiency under hard physical constraints (deadlines, non-overlapping servers, carrying capacities, and network topologies). Rather than ad-hoc programming, this assignment enforces structured pseudocode conforming to the **SIMATS Engineering Handbook for Algorithmic Pseudocode**.

---

## 3. SIMATS Engineering Pseudocode Standards

All pseudocode adheres to the following engineering conventions:
- **Strict Typing & Signatures:** Explicit `INPUT`, `OUTPUT`, and preconditions.
- **Forbidden Colloquialisms:** Elimination of ambiguous statements such as *"choose best item"* or *"process appropriately"*.
- **Standard Control Structures:** Capitalized keywords (`FOR`, `WHILE`, `IF ... THEN ... ELSE`, `RETURN`).
- **Mathematical Integrity:** Explicit indexing, bounds, and deterministic state updates.

---

## 4. Complete Task Solutions & Forensic Analyses


---

# TASK 1 – ALGORITHM DESIGN REVIEW: Diagnose and Repair Poor Pseudocode (6 Marks)

### Problem Context
A delivery vehicle has capacity $W$. Packages have weight $w_i$ and value $v_i$. Packages may be divided fractionally. The objective is to maximize the total value loaded without exceeding capacity $W$.

### Task 1.1 – Diagnose the Design (2 Marks)
The proposed pseudocode:
```
ALGORITHM LoadVehicle
BEGIN
 Read packages
 Arrange packages
 Select the best package
 WHILE vehicle has space DO
  Add suitable package
 END WHILE
 Calculate value
 RETURN result
END
```
**Algorithmic Deficiencies:**
1. **Inputs and Outputs Undefined:** The algorithm signature does not specify parameters (package set $P$, weights $W$, values $V$, knapsack capacity $C$) nor return structures.
2. **Ambiguous Selection Criterion ("best" / "suitable"):** The term "best package" is undefined—it does not state whether it sorts by maximum value $v_i$, minimum weight $w_i$, or value-to-weight density $v_i / w_i$.
3. **No Feasibility Condition or Capacity Tracking:** It does not maintain or decrement remaining capacity $C_{rem}$ as items are placed into the vehicle.
4. **Failure to Handle Fractional Division:** The requirement explicitly states packages may be divided if necessary, but the loop contains no fractional split logic when an item exceeds remaining space.
5. **Indefinite Termination / Potential Infinite Loop:** "WHILE vehicle has space DO" does not specify what happens if all items are packed or if no remaining unpacked package fits, leading to infinite looping or undefined indexing.

### Task 1.2 – Repair the Design (3 Marks)
Rewritten complete, language-independent pseudocode following SIMATS Engineering Standard:
```
ALGORITHM FractionalKnapsack(Packages, Capacity)
INPUT:
  Packages: Array of tuples (id, weight, value) of size n
  Capacity: Real number > 0 representing maximum vehicle capacity
OUTPUT:
  TotalValue: Real number representing maximum value loaded
  Solution: Array of tuples (id, fraction_loaded)

BEGIN
  // Step 1: Compute value-to-weight density for each package
  FOR i ← 1 TO n DO
    density[i] ← Packages[i].value / Packages[i].weight
  END FOR

  // Step 2: Sort packages in descending order of density
  SORT Packages in descending order of density

  // Step 3: Initialize tracking variables
  RemainingCapacity ← Capacity
  TotalValue ← 0.0
  Solution ← EMPTY_LIST()

  // Step 4: Greedy selection loop
  FOR i ← 1 TO n DO
    IF RemainingCapacity = 0 THEN
      BREAK
    END IF

    IF Packages[i].weight <= RemainingCapacity THEN
      // Item completely fits
      RemainingCapacity ← RemainingCapacity - Packages[i].weight
      TotalValue ← TotalValue + Packages[i].value
      APPEND(Solution, (Packages[i].id, 1.0))
    ELSE
      // Item must be fractionally divided to fill exact space
      fraction ← RemainingCapacity / Packages[i].weight
      TotalValue ← TotalValue + (Packages[i].value * fraction)
      APPEND(Solution, (Packages[i].id, fraction))
      RemainingCapacity ← 0
      BREAK
    END IF
  END FOR

  RETURN TotalValue, Solution
END
```

### Task 1.3 – Design Defence (1 Mark)
This rewritten design qualifies as pseudocode rather than programming code because it relies on standard algorithmic notations (such as explicit mathematical loops, clear variable scoping, and high-level abstractions like `SORT ... descending`) without binding to language-specific syntaxes, pointers, or library imports. It avoids informal English by providing exact arithmetic updates, definitive state transitions, and deterministic termination bounds.


---

# TASK 2 – FROM BUSINESS REQUIREMENT TO GREEDY PSEUDOCODE: Job Sequencing with Deadlines (8 Marks)

### Task 2.1 – Model the Requirement (2 Marks)
- **Input:** A set of $n$ computational jobs where each job $i$ has an identifier $J_i$, deadline $d_i \in \mathbb{Z}^+$, and profit $p_i \ge 0$.
- **Output:** An ordered schedule of scheduled jobs across time slots and total earned profit.
- **Objective:** Maximize total profit $\sum_{j \in 	ext{Scheduled}} p_j$.
- **Constraints:**
  - Each job takes exactly 1 discrete time slot.
  - At most 1 job can be executed in any time slot $[t-1, t]$.
  - A job $J_i$ earns profit $p_i$ only if completed at time $t \le d_i$.
- **Decision to be Made:** For each high-profit candidate job, decide whether a free time slot exists on or before its deadline, and schedule it in the latest available feasible slot.
- **Required Information:** A schedule slot map $	ext{Slot}[1 \dots \max(d_i)]$ initialized to empty.

### Task 2.2 – Formulate a Greedy Hypothesis (1 Mark)
**Greedy-Choice Rule:** "Consider jobs in non-increasing order of profit, and schedule each job in the latest available unoccupied time slot before or on its deadline."
**Justification:** Greedily committing to the highest-profit job maximizes instantaneous revenue gain, while placing it in the latest permissible slot preserves earlier slots for jobs with tighter deadlines.

### Task 2.3 – Design the Algorithm (3 Marks)
```
ALGORITHM JobSequencingWithDeadlines(Jobs, n)
INPUT:
  Jobs: Array of records (id, deadline, profit) for i = 1 to n
OUTPUT:
  Schedule: Array of job ids indexed by time slot 1 to max_deadline
  TotalProfit: Total earned profit

BEGIN
  SORT Jobs in descending order of profit

  max_deadline ← 0
  FOR i ← 1 TO n DO
    IF Jobs[i].deadline > max_deadline THEN
      max_deadline ← Jobs[i].deadline
    END IF
  END FOR

  FOR t ← 1 TO max_deadline DO
    Slot[t] ← NULL
  END FOR

  TotalProfit ← 0

  FOR i ← 1 TO n DO
    // Greedily find latest available slot <= deadline
    FOR t ← MIN(max_deadline, Jobs[i].deadline) DOWNTO 1 DO
      IF Slot[t] = NULL THEN
        Slot[t] ← Jobs[i].id
        TotalProfit ← TotalProfit + Jobs[i].profit
        BREAK
      END IF
    END FOR
  END FOR

  RETURN Slot, TotalProfit
END
```

### Task 2.4 – Desk-Check (1 Mark)
Given instance:
| Job | Deadline | Profit |
|---|---|---|
| A | 2 | 80 |
| B | 1 | 35 |
| C | 2 | 60 |
| D | 3 | 40 |
| E | 1 | 25 |

- **Sorted order by profit:** A(80, d=2), C(60, d=2), D(40, d=3), B(35, d=1), E(25, d=1). Max deadline $= 3$. Slots: `[1: NULL, 2: NULL, 3: NULL]`.
- **Job A:** deadline 2 $	o$ inspect slot 2 (free) $	o$ `Slot[2] = A`, Profit $= 80$.
- **Job C:** deadline 2 $	o$ inspect slot 2 (occupied) $	o$ inspect slot 1 (free) $	o$ `Slot[1] = C`, Profit $= 80 + 60 = 140$.
- **Job D:** deadline 3 $	o$ inspect slot 3 (free) $	o$ `Slot[3] = D`, Profit $= 140 + 40 = 180$.
- **Job B:** deadline 1 $	o$ inspect slot 1 (occupied) $	o$ rejected.
- **Job E:** deadline 1 $	o$ inspect slot 1 (occupied) $	o$ rejected.
- **Final Schedule:** Slot 1: C, Slot 2: A, Slot 3: D. **Total Profit = 180**.

### Task 2.5 – Challenge Your Design (1 Mark)
- **Modified Instance:** Change Job B's deadline from 1 to 3 ($d_B = 3$) with profit 70 (higher than C and D).
- **Prediction:** Job B will now take slot 3, preempting Job D.
- **Verification:** Jobs sorted: A(80, d=2), B(70, d=3), C(60, d=2), D(40, d=3), E(25, d=1). Slot 2 gets A, Slot 3 gets B, Slot 1 gets C. Total Profit $= 80 + 70 + 60 = 210$. Prediction confirmed.


---

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


---

# TASK 4 – PSEUDOCODE FORENSICS: Find, Explain and Repair an Algorithmic Defect (7 Marks)

### Task 4.1 – Locate the Defect (2 Marks)
The flawed logic is in line 5 of inner loop:
```
IF substring(Text, j, i) is in Dictionary THEN
  DP[i] ← TRUE
  BREAK
END IF
```
**Exact Defect:** The condition only checks if substring $(j, i)$ is in Dictionary, without verifying whether the prefix string before $j$ is validly segmented ($DP[j] == 	ext{TRUE}$). Finding a dictionary word from index $j$ to $i$ is completely useless if the prefix up to $j$ cannot be formed from valid dictionary words!

### Task 4.2 – Construct a Failing Input (2 Marks)
- **Text:** `"catsandog"` ($n=9$).
- **Dictionary:** `{"cats", "dog", "sand", "and", "cat"}`.
- **Trace of Flaw:**
  At $i=9$, the faulty algorithm checks substring $(6, 9) = 	ext{"dog"}$.
  Because `"dog"` is in Dictionary, the algorithm sets $DP[9] \leftarrow 	ext{TRUE}$ and terminates with TRUE.
  However, the prefix from $0$ to $6$ is `"catsan"`, which CANNOT be segmented! The word `"og"` or disjoint characters cannot be formed. The true answer is FALSE.

### Task 4.3 – Repair the Algorithm (2 Marks)
Minimal correction: Add `$DP[j]$ AND` to the condition:
```
ALGORITHM WordBreak_Repaired(Text, Dictionary)
BEGIN
  DP[0] ← TRUE
  FOR i ← 1 TO n DO
    DP[i] ← FALSE
    FOR j ← 0 TO i - 1 DO
      IF DP[j] AND (substring(Text, j, i) is in Dictionary) THEN
        DP[i] ← TRUE
        BREAK
      END IF
    END FOR
  END FOR
  RETURN DP[n]
END
```

### Task 4.4 – Regression Check (1 Mark)
- **Input:** Text: `"leetcode"`, Dictionary: `{"leet", "code"}`.
- **Trace on Repaired:**
  - $i=4$: $j=0 \implies DP[0]=	ext{TRUE}$ and `"leet"` in Dict $\implies DP[4]=	ext{TRUE}$.
  - $i=8$: $j=4 \implies DP[4]=	ext{TRUE}$ and `"code"` in Dict $\implies DP[8]=	ext{TRUE}$.
- **Result:** Returns TRUE, correctly preserving valid behavior.


---

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


---

# TASK 6 – DESIGN CHALLENGE: Energy-Aware Job Scheduling in a Cloud Data Centre (13 Marks)

### Stage 1 – Interpret the Problem (2 Marks)
- **Input:** $n$ independent computational jobs. Each job $J_i = (s_i, f_i, v_i)$, where $s_i$ is start time, $f_i$ is finish time ($f_i > s_i$), and $v_i$ is the energy-saving value.
- **Output:** A compatible subset of jobs $S \subseteq \{1 \dots n\}$ and total energy saved.
- **Objective:** Maximize total energy savings $\sum_{i \in S} v_i$.
- **Constraints:** Non-overlapping constraint: for any two distinct scheduled jobs $J_a, J_b \in S$, either $f_a \le s_b$ or $f_b \le s_a$. At most one job runs on the server at any point.

### Stage 2 – Propose the Strategy (2 Marks)
- **Investigation of Greedy Heuristics:**
  - Earliest finish time (unweighted interval scheduling): Fails because a short job with tiny value could block high-value jobs.
  - Highest value first: Fails because a high-value job could overlap and block multiple jobs whose sum of values is greater.
- **Selected Strategy:** **Dynamic Programming with Binary Search (Weighted Interval Scheduling)**.
- **Justification:** The problem exhibits optimal substructure and overlapping subproblems. A job $i$ either belongs to the optimal subset or it does not. If included, the remaining optimal schedule consists of the optimal solution among all jobs that finish before job $i$ starts.

### Stage 3 – Identify Critical Information (2 Marks)
- **Preprocessing:** Sort all jobs in non-decreasing order of finish time: $f_1 \le f_2 \le \dots \le f_n$.
- **Predecessor Array $p[i]$:** Let $p[i]$ be the largest index $j < i$ such that job $j$ is mutually compatible with job $i$ ($f_j \le s_i$). Computed via binary search in $O(\log n)$.
- **State Formulation:** $OPT[i]$ stores the maximum energy-saving value achievable from a valid subset of jobs chosen from $\{J_1, \dots, J_i\}$.
- **Base Condition:** $OPT[0] = 0$.
- **Recurrence:**
  $$OPT[i] = \max(OPT[i-1], \ v_i + OPT[p[i]])$$

### Stage 4 – Design Complete Pseudocode (4 Marks)
```
ALGORITHM WeightedIntervalScheduling(Jobs, n)
INPUT:
  Jobs: Array of records (id, start, finish, value) for i = 1 to n
OUTPUT:
  MaxEnergySaved: Maximum achievable energy saving
  SelectedJobs: List of job IDs included in optimal schedule

BEGIN
  // Step 1: Sort jobs by finish time ascending
  SORT Jobs in ascending order of finish_time

  // Step 2: Compute compatible predecessor p[i] using binary search
  p[0] ← 0
  FOR i ← 1 TO n DO
    p[i] ← BINARY_SEARCH_PREDECESSOR(Jobs, i)
  END FOR

  // Step 3: Compute DP array
  OPT[0] ← 0
  FOR i ← 1 TO n DO
    include_val ← Jobs[i].value + OPT[p[i]]
    exclude_val ← OPT[i - 1]
    IF include_val > exclude_val THEN
      OPT[i] ← include_val
    ELSE
      OPT[i] ← exclude_val
    END IF
  END FOR

  MaxEnergySaved ← OPT[n]

  // Step 4: Backtrack to reconstruct selected jobs
  SelectedJobs ← EMPTY_LIST()
  curr ← n
  WHILE curr > 0 DO
    IF Jobs[curr].value + OPT[p[curr]] > OPT[curr - 1] THEN
      APPEND(SelectedJobs, Jobs[curr].id)
      curr ← p[curr]
    ELSE
      curr ← curr - 1
    END IF
  END WHILE

  RETURN MaxEnergySaved, REVERSE(SelectedJobs)
END

FUNCTION BINARY_SEARCH_PREDECESSOR(Jobs, i)
  low ← 1; high ← i - 1; ans ← 0
  WHILE low <= high DO
    mid ← (low + high) / 2
    IF Jobs[mid].finish <= Jobs[i].start THEN
      ans ← mid
      low ← mid + 1
    ELSE
      high ← mid - 1
    END IF
  END WHILE
  RETURN ans
END
```

### Stage 5 – Desk-Check (1 Mark)
Dataset provided in assessment:
| Job | Start | Finish | Value | $p[i]$ | $v_i + OPT[p[i]]$ | $OPT[i-1]$ | $OPT[i]$ |
|---|---|---|---|---|---|---|---|
| J1 | 1 | 3 | 20 | 0 | 20 | 0 | 20 |
| J2 | 2 | 5 | 50 | 0 | 50 | 20 | 50 |
| J3 | 4 | 6 | 30 | 1 (J1) | $30+20=50$ | 50 | 50 |
| J4 | 6 | 8 | 40 | 3 (J3) | $40+50=90$ | 50 | 90 |
| J5 | 5 | 9 | 60 | 2 (J2) | $60+50=110$ | 90 | 110 |
| J6 | 8 | 10 | 30 | 4 (J4) | $30+90=120$ | 110 | 120 |
| J7 | 9 | 11 | 50 | 5 (J5) | $50+110=160$ | 120 | 160 |
| J8 | 11 | 13 | 40 | 7 (J7) | $40+160=200$ | 160 | 200 |

- **Reconstruction:**
  - $i=8$: Include J8 ($v_8 + OPT[7] = 200 > OPT[7]=160$) $	o$ Next $p[8] = 7$.
  - $i=7$: Include J7 ($v_7 + OPT[5] = 160 > OPT[6]=120$) $	o$ Next $p[7] = 5$.
  - $i=5$: Include J5 ($v_5 + OPT[2] = 110 > OPT[4]=90$) $	o$ Next $p[5] = 2$.
  - $i=2$: Include J2 ($v_2 + OPT[0] = 50 > OPT[1]=20$) $	o$ Next $p[2] = 0$.
- **Selected Jobs:** **J2, J5, J7, J8**.
- **Total Energy Saved:** $50 + 60 + 50 + 40 = \mathbf{200}$.

### Stage 6 – Attack Your Own Design (2 Marks)
- **Adversarial Construction:**
  - A1: [1, 10], Value = 100 (Locally massive single value).
  - B1: [1, 3], Value = 40
  - B2: [3, 5], Value = 40
  - B3: [5, 7], Value = 40
  - B4: [7, 10], Value = 40
- **Why Challenging:** Greedy by value immediately picks A1 (value 100).
- **Behavior of our DP Algorithm:**
  $OPT$ for B-chain accumulates: $40 + 40 + 40 + 40 = 160 > 100$.
  The algorithm evaluates $\max(OPT[B_4] + v(A1), \dots)$ and selects the $\{B_1, B_2, B_3, B_4\}$ set, correctly yielding 160. The adversarial attack fails to defeat the algorithm because DP systematically explores the inclusion/exclusion state-space.

---

## 5. Comparative Analysis of Greedy vs Dynamic Programming

| Architectural Dimension | Greedy Strategy | Dynamic Programming |
|---|---|---|
| **Fundamental Invariant** | Makes locally optimal choice at each step; never reconsiders previous choices. | Explores all feasible subproblems; combines optimal solutions of overlapping subproblems. |
| **Prerequisite Property** | **Greedy-Choice Property** + Optimal Substructure. | **Overlapping Subproblems** + Optimal Substructure. |
| **State Tracking** | Single accumulator variable; $O(1)$ state. | Multi-dimensional memoization table; $O(n \cdot W)$ or $O(n^2)$ state. |
| **Computational Cost** | Typically $O(n \log n)$ due to initial sorting. | Pseudo-polynomial or polynomial ($O(n \cdot W)$, $O(n^3)$). |
| **Optimality Failure Mode** | Fails when local choices lock out superior global combinations (e.g., 0/1 Knapsack). | Guaranteed optimal; failure occurs only if recurrence or base state is malformed. |

---

## 6. Adversarial Testing & Boundary Verification

1. **Fractional Knapsack (Task 1):** Validated on capacity exhaustion where remaining capacity is strictly smaller than package weight. Fractional split rule correctly divides package without precision overflow.
2. **Job Scheduling (Task 2):** Tested against tightly nested deadlines where earlier tasks contend for slot 1. Reverse-deadline scan successfully preserves free slots for preceding tasks.
3. **WordBreak Forensics (Task 4):** Adversarial string `"catsandog"` with dictionary `{"cats", "dog", "sand", "and", "cat"}` completely exposed the flawed algorithm, while the repaired algorithm returned `FALSE` correctly.
4. **Energy Scheduling (Task 6):** An adversarial job with value 100 spanning the entire window was defeated by a chain of four 40-value non-overlapping jobs (Total = 160), proving that DP systematically explores optimal combinations.

---

## 7. Conclusion & Technical Reflection

Algorithmic design through rigorous pseudocode serves as the critical bridge between abstract problem specifications and robust software implementations. By diagnosing flaws, formalizing recurrences, and proving invariants before writing code, engineers avoid catastrophic defects in production systems.

---

## 8. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. Kleinberg, J., & Tardos, É. (2006). *Algorithm Design*. Pearson.
3. SIMATS Engineering. *Handbook for Algorithmic Pseudocode and Design Standards*.
