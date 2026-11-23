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
