# TASK 4 – SMART MANUFACTURING OPTIMISATION: Assembly Line Scheduling (7 Marks)

### Task 4.1 – Build the Optimisation Engine (3 Marks)
- 2 parallel assembly lines, 4 stations each.
- Line 1 processing times: `[4, 5, 3, 2]`; Line 2: `[2, 10, 1, 4]`.
- Transfer times: $T_{1 	o 2} = [7, 4, 2]$; $T_{2 	o 1} = [9, 2, 8]$. Entry: $e_1=10, e_2=12$; Exit: $x_1=18, x_2=7$.
- **Optimal Route:** Entry $	o$ Line 1, Station 1 $	o$ Line 1, Station 2 $	o$ Transfer to Line 2, Station 3 $	o$ Line 2, Station 4 $	o$ Exit.
- **Minimum Production Time:** **35**.

### Task 4.2 – Expose the Decision Process (1 Mark)
| Station | Reach Line 1 by Staying | Reach Line 1 by Transfer | Selected | Reach Line 2 by Staying | Reach Line 2 by Transfer | Selected |
|---|---|---|---|---|---|---|
| 2 | $14 + 5 = 19$ | $14 + 9 + 5 = 28$ | Line 1 (Stay) | $14 + 10 = 24$ | $14 + 7 + 10 = 31$ | Line 2 (Stay) |
| 3 | $19 + 3 = 22$ | $24 + 2 + 3 = 29$ | Line 1 (Stay) | $24 + 1 = 25$ | $19 + 4 + 1 = 24$ | Line 1 (Transfer) |
| 4 | $22 + 2 = 24$ | $24 + 8 + 2 = 34$ | Line 1 (Stay) | $24 + 4 = 28$ | $22 + 2 + 4 = 28$ | Tie / Line 1 |

### Task 4.3 – Predict Before You Execute (1 Mark)
- Substantially increased transfer time $T_{1 	o 2}[2]$ from 4 to 20.
- **Prediction:** The transfer from Line 1 to Line 2 at Station 3 will become disadvantageous; production will stay on Line 1. Total time will increase.
- **Observed:** Optimal route switches to staying purely on Line 1 until station 4. Minimum time increases to 42.

### Task 4.4 – Production Disruption Challenge (1 Mark)
- Station 2 on Line 1 disrupted (time increased from 5 to 25).
- **Result:** The engine moves production to Line 2 at Station 2, bypassing the bottleneck.

### Task 4.5 – Engineering Extension: Three Assembly Lines (1 Mark)
- **DP State:** Let $f_k[j]$ be the minimum time to complete processing through station $j$ on line $k \in \{1, 2, 3\}$.
- **Transition:** For each line $k$:
  $$f_k[j] = \min_{m \in \{1, 2, 3\}} (f_m[j-1] + t_{m, k}[j-1]) + a_k[j]$$
  where $t_{m, k} = 0$ if $m = k$.
- **Reconstruction:** A predecessor table $l_k[j] \in \{1, 2, 3\}$ records the winning predecessor line.
