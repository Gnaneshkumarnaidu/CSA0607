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
